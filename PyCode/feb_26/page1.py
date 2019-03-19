def createParagraphTag(data):
    print('<p>{}</p>'.format(data))

def createDivTag(data):
    print('<div>{}</div>'.format(data))

def createHeaderTag(data):
    print('<h1>{}</h1>'.format(data))

# createParagraphTag('this is a para 1')
# createParagraphTag('this is a para 2')
#
# createDivTag('this is a div 1')
# createDivTag('this is a div 2')
#
# createHeaderTag('this is a header 1')
# createHeaderTag('this is a header 2')


def createTag1(tagName, data):
    print('<{}>{}</{}>'.format(tagName, data, tagName))

# createTag1('p', 'this is a para 1')
# createTag1('p', 'this is a para 2')
#
# createTag1('div', 'this is a div 1')
# createTag1('div', 'this is a div 2')
#
# createTag1('h1', 'this is a header 1')
# createTag1('h1', 'this is a header 2')


def createTag(tagName):
    def inner(data):
        print('<{}>{}</{}>'.format(tagName, data, tagName))

    return inner

p = createTag('p')
p('this is a para 1')
p('this is a para 2')

div = createTag('div')
div('this is div 1')
div('this is div 2')

h1 = createTag('h1')
h1('this is header 1')



