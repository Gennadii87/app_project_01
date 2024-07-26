from django import template
from django.urls import resolve
from ..models import Menu, MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_all_menus(context):
    request = context['request']
    current_url = request.path

    menus_data = {}

    all_menus = Menu.objects.all()

    for menu in all_menus:
        def get_menu_items(parent=None):
            return MenuItem.objects.filter(menu=menu, parent=parent).order_by('id')

        def get_active_items(menu_items):
            active_items = []
            for item in menu_items:
                item_url = item.get_url()
                # Debug output to verify URL matching
                print(f"Checking item URL: {item_url} with current URL: {current_url}")
                if item_url == current_url or current_url.startswith(item_url):
                    active_items.append(item)
                    active_items.extend(get_active_items(item.children.all()))
            return active_items

        active_items = get_active_items(get_menu_items())
        menus_data[menu.name] = {
            'menu': menu,
            'active_items': active_items,
            'items': get_menu_items(),
        }

    return menus_data

