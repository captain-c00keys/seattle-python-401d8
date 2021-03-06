from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import NO_PERMISSION_REQUIRED


@view_config(route_name='home', renderer='../templates/base.jinja2', permission=NO_PERMISSION_REQUIRED)
def home_view(request):
    """Returns homepage."""

    if request.authenticated_userid is not None:
        return HTTPFound(location=request.route_url('portfolio'))

    return {}
