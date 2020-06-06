
def get_breaks(content,length):
    data = ""
    words = content.split(' ')
    total_chars = 0
    for i in range(len(words)):
        total_chars += len(words[i])
        if total_chars > length:
            data = data + "<br>" + words[i]
            total_chars = 0
        else:
            data += " " + words[i]
    return data
