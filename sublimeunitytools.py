import sublime, sublime_plugin

import os

class SwitchToMetaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current_file = self.view.file_name()

        if current_file is None:
            return

        go_to_file = current_file + '.meta'

        if go_to_file is None or not os.path.isfile(go_to_file):
            return

        print("SwitchToMetaCommand  " + str(go_to_file))
        self.view.window().open_file(go_to_file)



class SwitchFromMetaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current_file = self.view.file_name()

        if current_file is None:
            return

        if current_file[len(current_file)-5:] == '.meta':
            go_to_file = current_file[:len(current_file)-5]

            if go_to_file is None or not os.path.isfile(go_to_file):
                return

            print("SwitchFromMetaCommand  " + str(go_to_file))
            self.view.window().open_file(go_to_file)