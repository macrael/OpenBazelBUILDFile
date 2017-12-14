#!/usr/bin/env python3

import sublime
import sublime_plugin
import os


def _find_build_file(check_directory):
    check_path = os.path.join(check_directory, 'BUILD')
    if os.path.isfile(check_path):
        return check_path
    elif check_directory == os.path.sep:
        return None
    else:
        return _find_build_file(os.path.dirname(check_directory))


class OpenBuildFileCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        active_file_path = self._active_file_path()
        check_directory = os.path.dirname(active_file_path)
        build_path = _find_build_file(check_directory)
        if build_path is None:
            sublime.status_message('No BUILD file found in this or any super-directory.')
        else:
            self.window.open_file(build_path)

    # Returns the activelly open file path from sublime.
    def _active_file_path(self):
        if self.window.active_view():
            file_path = self.window.active_view().file_name()

            if file_path and len(file_path) > 0:
                return file_path
