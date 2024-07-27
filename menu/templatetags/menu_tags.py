from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_all_menus(context):
    request = context['request']
    current_url = request.path

    menus_data = {}
    selected_item = None

    all_menus = Menu.objects.all()

    for menu in all_menus:
        def get_menu_items(parent=None):
            return MenuItem.objects.filter(menu=menu, parent=parent).order_by('id')

        def get_active_items(menu_items):
            active_items = []
            nonlocal selected_item

            for item in menu_items:
                item_url = item.get_url()
                if item_url == current_url:
                    active_items.append(item)
                    selected_item = item

                active_items.extend(get_active_items(item.children.all()))

            return active_items

        active = get_active_items(get_menu_items())

        menus_data[menu.name] = {
            'menu': menu,
            'active': active,
            'items': get_menu_items(),
        }

    context['selected_item'] = selected_item
    return menus_data
