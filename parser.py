
with open('MirasText.txt', 'r', encoding='utf8') as file:
    for line in file:
        tokens = line.split('***')
        content = tokens[0]
        description = tokens[1]
        keywords = tokens[2]
        title = tokens[3]
        website = tokens[4]
        url = tokens[5]

        print('content : ' + content)
        print('description : ' + description)
        print('keywords : ' + keywords)
        print('title : ' + title)
        print('website : ' + website)
        print('url : ' + url)
