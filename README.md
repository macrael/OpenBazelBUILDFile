Open Bazel BUILD File
=====================

Open Bazel BUILD File is a plugin for Sublime Text that opens the related bazel BUILD file for the current open file.

It's very simple, it looks for a BUILD file in the directory with the open file, then recurses up subdirectories until it find ones, and opens it. It's nice that you can immediately switch back to the formerly open file by using super + t, return.

The keymap is ctrl + super + b, and the command name is `open_build_file`
