from django import template
from wagtail.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_menu_items(context):
    """
    Wagtail has a specific property for pages that are in the menu called "in_menu"
    """

    home_page = Site.find_for_request(context.request).root_page
    menu_items = home_page.get_children().in_menu().live()
    return [home_page] + [item for item in menu_items]
