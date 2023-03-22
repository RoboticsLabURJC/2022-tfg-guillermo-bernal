# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/guillermo/tello_ws/src/tello_ros/tello_description

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/guillermo/tello_ws/build/tello_description

# Utility rule file for generate_urdf.

# Include any custom commands dependencies for this target.
include CMakeFiles/generate_urdf.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/generate_urdf.dir/progress.make

CMakeFiles/generate_urdf: urdf/tello.urdf

urdf/tello.urdf: /home/guillermo/tello_ws/src/tello_ros/tello_description/urdf/tello.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/guillermo/tello_ws/build/tello_description/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generate /home/guillermo/tello_ws/build/tello_description/urdf/tello.urdf"
	/home/guillermo/tello_ws/src/tello_ros/tello_description/src/replace.py /home/guillermo/tello_ws/src/tello_ros/tello_description/urdf/tello.xml suffix= topic_ns=solo > /home/guillermo/tello_ws/build/tello_description/urdf/tello.urdf

generate_urdf: CMakeFiles/generate_urdf
generate_urdf: urdf/tello.urdf
generate_urdf: CMakeFiles/generate_urdf.dir/build.make
.PHONY : generate_urdf

# Rule to build all files generated by this target.
CMakeFiles/generate_urdf.dir/build: generate_urdf
.PHONY : CMakeFiles/generate_urdf.dir/build

CMakeFiles/generate_urdf.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/generate_urdf.dir/cmake_clean.cmake
.PHONY : CMakeFiles/generate_urdf.dir/clean

CMakeFiles/generate_urdf.dir/depend:
	cd /home/guillermo/tello_ws/build/tello_description && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/guillermo/tello_ws/src/tello_ros/tello_description /home/guillermo/tello_ws/src/tello_ros/tello_description /home/guillermo/tello_ws/build/tello_description /home/guillermo/tello_ws/build/tello_description /home/guillermo/tello_ws/build/tello_description/CMakeFiles/generate_urdf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/generate_urdf.dir/depend

