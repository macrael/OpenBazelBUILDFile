import sublime_plugin
import os


def _find_build_file(check_directory):
    check_path_bare = os.path.join(check_directory, 'BUILD')
    check_path_ext = os.path.join(check_directory, 'BUILD.bazel')
    if os.path.isfile(check_path_bare):
        return check_path_bare
    elif os.path.isfile(check_path_ext):
        return check_path_ext
    elif os.path.dirname(check_directory) == check_directory:
        return None
    else:
        return _find_build_file(os.path.dirname(check_directory))


class OpenBazelBuildFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        if file_path:
            check_directory = os.path.dirname(file_path)
            build_path = _find_build_file(check_directory)
            if build_path is None:
                self.view.window().status_message('No BUILD file found in this or any super-directory.')
            else:
                self.view.window().open_file(build_path)
