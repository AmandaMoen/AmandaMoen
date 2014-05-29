class Element(object):

    tag = u''
    indent = u'    '

    def __init__(self, content = None, **kwargs):

        if content is not None:
            self.content = [content]
        else:
            self.content = []

        self.html_attributes_dict = kwargs


    def append(self, string):
        self.content.append(string)


    def render(self, file_out, ind = ""):

        #ind = amount of indent "so far"
        html_attributes_string = u""
        for key, value in self.html_attributes_dict.iteritems():
            html_attributes_string = html_attributes_string + ' {0}="{1}"'.format(key,value)

        # Write the opening tag
        file_out.write('{0}<{1}{2}>\n'.format(ind, self.tag, html_attributes_string))

        # Iterate through the items in list self.content
        for item in self.content:
            #print item

            # If item is tag, render it this way
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            
            # Otherwise item is NOT a tag, so render it differently
            else:
                file_out.write(ind + self.indent + item + '\n')

        # Write the closing tag
        file_out.write('{0}</{1}>\n'.format(ind, self.tag))


class Html(Element):
    tag = u'html'

    # Override Element's render() method
    def render(self, file_out, ind = ""):

        # Write the initial doctype tag
        file_out.write('<!DOCTYPE html>\n')

        # Call to super (which is an instance of Element's render() method) to render <html> tags
        super(Html, self).render(file_out = file_out, ind = ind)


class Head(Element):
    tag = u'head'


class OneLineTag(Element):

    # Override render method to render everything on one line
    def render(self, file_out, ind = ""):

       #ind = amount of indent "so far"
        html_attributes_string = u""
        for key, value in self.html_attributes_dict.iteritems():
            html_attributes_string = html_attributes_string + ' {0}="{1}"'.format(key,value)

        # Write the opening tag
        file_out.write('{0}<{1}{2}>'.format(ind, self.tag, html_attributes_string))

        # Iterate through the items in list self.content
        for item in self.content:

            # If item is tag, render it this way
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            
            # Otherwise item is NOT a tag, so render it differently
            else:
                file_out.write(item)

        # Write the closing tag
        file_out.write('</{0}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = u'title'


class Body(Element):
    tag = u'body'


class P(Element):
    tag = u'p'


class SelfClosingTag(Element):

    # Override render method to accommodate self closing tags
    def render(self, file_out, ind = ""):
        #ind = amount of indent "so far"
        html_attributes_string = u""
        for key, value in self.html_attributes_dict.iteritems():
            html_attributes_string = html_attributes_string + '{0}="{1}"'.format(key,value)

        # Write the self closing tag
        file_out.write('{0}<{1} {2}/>\n'.format(ind, self.tag, html_attributes_string))


class Hr(SelfClosingTag):
    tag = u'hr'


class Br(SelfClosingTag):
    tag = u'br'


class A(Element):
    tag = u'a'

    def __init__(self, link, content, **kwargs):

        # Add an item to the kwargs dict, with a key of 'href' and a value of the incoming link
        kwargs['href'] = link

        # Call the __init__ method of super(), and pass content and kwargs (which now contains a key of 'href' with a value of link)
        super(A, self).__init__(content = content, **kwargs)

        # Output should look like this:
        # And this is a 
        # <a href="http://google.com">link</a>
        # to google


class Ul(Element):
    tag = u'ul'


class Li(Element):
    tag = u'li'


class H(OneLineTag):

    def __init__(self, header_level, content, **kwargs):

        self.tag = u'h' + str(header_level)

        super(H, self).__init__(content = content, **kwargs)


class Meta(SelfClosingTag):
    tag = u'meta'