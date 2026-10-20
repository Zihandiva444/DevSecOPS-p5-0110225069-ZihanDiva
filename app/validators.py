def validate_title(title):
    if not isinstance(title, str):
        return False, "Title harus berupa teks"
    title = title.strip()
    if len(title) == 0:
        return False, "Title tidak boleh kosong"
    if len(title) > 100:
        return False, "Title maksimal 100 karakter"
    return True, title