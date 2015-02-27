[![Build Status](https://travis-ci.org/arve0/codeclub_lesson_builder.svg?branch=nb-NO)](https://travis-ci.org/arve0/codeclub_lesson_builder)

This is a recipe of how you can create your own code club lesson
pages with [codeclub_lesson_builder](https://github.com/arve0/codeclub_lesson_builder).

See the result [here](http://arve0.github.io/example_lessons/).

This repo has been bootstrapped like this:
```shell
# clone empty repo
git clone https://github.com/arve0/example_lessons
cd example_lessons/

# clone builder
git clone --depth 1 https://github.com/arve0/codeclub_lesson_builder

# get UK lessons
git clone --depth 1 https://github.com/CodeClub/python-curriculum
git clone --depth 1 https://github.com/CodeClub/webdev-curriculum
git clone --depth 1 https://github.com/CodeClub/scratch-curriculum

# copy english lessons to src folder
mkdir src
cp -r python-curriculum/en-GB/ src/python
cp -r scratch-curriculum/en-GB/ src/scratch
cp -r webdev-curriculum/en-GB/ src/web

# fix format of yaml headers and code blocks
find src/ -name "*.md" -print0 | xargs -0 -L 1 codeclub_lesson_builder/utils/fix_yaml_header.sh 
find src/ -name "*.md" -print0 | xargs -0 -L 1 codeclub_lesson_builder/utils/fix_code_blocks.sh 

# fix YAML in one of the files manually
sed -i '' 's/\.\.\./---/g' src/python/lessons/Minecraft2D/Minecraft2D.md

# create index.md
echo -e "---\ntitle: welcome\ntemplate: index.jade\n---\n# welcome\n... to this demo of [codeclub_lesson_builder](https://github.com/arve0/codeclub_lesson_builder)" > src/index.md

# copy setup script and run it
cp ./codeclub_lesson_builder/utils/setup .
./setup

# copy culp shortcuts and build
cp codeclub_lesson_builder/utils/gulp* .
./gulp
```
