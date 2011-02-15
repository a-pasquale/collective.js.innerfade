from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class FolderInnerfadeView(BrowserView):

    template = ViewPageTemplateFile('folder_innerfade_view.pt')

    def getImages(self):

        return self.context.listFolderContents(contentFilter={'portal_type':'Image'})

    def getLink(self, imageId):

        result = ''
        links = self.context.getFolderContents(contentFilter={'portal_type':'Link', 'id':imageId+'.link'})

        if links:
            result = links[0]

        return result
