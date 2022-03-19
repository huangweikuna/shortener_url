import json
import traceback

from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponseRedirect

from shortener.service import result
from shortener.service.shortener_service import ShortenerService

shortener_service = ShortenerService()


def new_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return result.ok(dict(code=shortener_service.new_url(data.get('url', '').strip())))
        except ValidationError as ve:
            return result.client_error(str(ve))
        except Exception as e:
            print(traceback.format_exc())
            return result.server_error(str(e))
    else:
        raise result.client_error("method error")


def redirect(request, code):
    try:
        url = shortener_service.get_url(code)
    except Exception as e:
        print(traceback.format_exc())
        return result.server_error(str(e))
    print(url)
    return HttpResponseRedirect(url)
