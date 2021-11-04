def get_selected_tags_from_request(request):
    tag_ids = request.GET.get('t')
    if not tag_ids:
        return None

    # sanitize tag ids
    id_to_tag = {t.id: t for t in request.tags}

    tags = []
    for data in tag_ids.split(','):
        try:
            tag_id = int(data)
            tags.append(id_to_tag[tag_id])
        except (ValueError, KeyError):
            continue
    return tags


def get_search_term_from_request(request):
    s = request.GET.get('s')
    if not s:
        return None
    return s
