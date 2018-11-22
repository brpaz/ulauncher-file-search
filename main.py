""" Main Module """

import logging
import os
import subprocess
# pylint: disable=import-error
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

LOGGING = logging.getLogger(__name__)

FILE_SEARCH_ALL = 'ALL'

FILE_SEARCH_DIRECTORY = 'DIR'

FILE_SEARCH_FILE = 'FILE'


class FileSearchExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(FileSearchExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def search(self, query, file_type=None):
        """ Searches for Files using fd command """
        cmd = ['fd', '-L']

        if file_type == FILE_SEARCH_FILE:
            cmd.append('-t')
            cmd.append('f')
        elif file_type == FILE_SEARCH_DIRECTORY:
            cmd.append('-t')
            cmd.append('d')

        cmd.append(query)
        cmd.append(self.preferences['base_dir'])

        process = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        out, err = process.communicate()

        if err:
            self.logger.error(err)
            return []

        files = out.split('\n')
        files = filter(None, files)  # remove empty lines

        result = []

        # pylint: disable=C0103
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension:
                icon = 'images/file.png'
            else:
                icon = 'images/folder.png'

            result.append({
                'path': f,
                'name': filename,
                'icon': icon
            })

        return result

    def get_open_in_terminal_script(self, path):
        """ Returns the script based on the type of terminal """
        terminal_emulator = self.preferences['terminal_emulator']

        # some terminals might work differently. This is already prepared for that.
        if terminal_emulator in ['gnome-terminal', 'terminator', 'tilix', 'xfce-terminal']:
            return RunScriptAction(terminal_emulator, ['--working-directory', path])

        return DoNothingAction()


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        items = []

        query = event.get_argument()

        if not query or len(query) < 3:
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name='Keep typing your search criteria ...',
                on_enter=DoNothingAction())])

        keyword = event.get_keyword()

        file_type = FILE_SEARCH_ALL
        if keyword == "ff":
            file_type = FILE_SEARCH_FILE
        elif keyword == "fdir":
            file_type = FILE_SEARCH_DIRECTORY

        results = extension.search(query.strip(), file_type)

        if not results:
            return RenderResultListAction([ExtensionResultItem(
                icon='images/icon.png',
                name='No Results found matching %s' % query,
                on_enter=HideWindowAction())])

        items = []
        for result in results[:15]:
            items.append(ExtensionSmallResultItem(
                icon=result['icon'],
                name=result['path'],
                on_enter=OpenAction(result['path']),
                on_alt_enter=extension.get_open_in_terminal_script(
                    result['path'])
            ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    FileSearchExtension().run()
