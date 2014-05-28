
#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = ''
    indent = "    "
    def __init__(self, content= None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        
        self.attributes = kwargs

    def render(self, file_out, ind = ""):
        attributes = ''
        for (k,v) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = k, value = v))
        file_out.write('\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item)
        file_out.write('\n%s</%s>' % (ind, self.tag))
    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = 'html'
    def render(self, file_out, ind = ""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self,file_out)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
class Head(Element):
    tag = 'head'
class OneLineTag(Element):
    def render(self, file_out, ind = ""):
        attributes = ''
        for (k,v) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = k, value = v))
        file_out.write('%s<%s%s>' % (ind, self.tag, attributes) )
        for item in self.content:
            try:

                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item)
        file_out.write('%s</%s>' % (ind, self.tag))
class Title(OneLineTag):
    tag = 'title'
class SelfClosingTag(Element):
    def render(self, file_out, ind = ""):
        attributes = ''
        for (k,v) in self.attributes.items():
            attributes += ' {key} = "{value}"'.format(key = k, value = v)
        file_out.write('\n%s<%s%s />\n' % (ind, self.tag, attributes))
class Hr(SelfClosingTag):
    tag = 'hr'
class Br(SelfClosingTag):
    tag = 'br'
class A(OneLineTag):
    tag = 'a'
    def __init__(self, link = None, content=None):
        link = dict(href = link)
        OneLineTag.__init__(self, content, **link)
class Ul(Element):
    tag = 'ul'
class Li(Element):
    tag = 'li'
class H(OneLineTag):
    def __init__(self, header_level, content=None):
        OneLineTag.__init__(self, content)
        #how to get the header level and pass it into the tag argument
        self.tag- = 'h%i' %header_level
class Meta(SelfClosingTag):
    tag = 'meta'
