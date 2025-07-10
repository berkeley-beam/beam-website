# beam-website

## Getting started

To do dev work for the site, pull the repo to your local machine.

The `GEMFILE.lock` contains all dependencies needed + the versions of those dependencies.

Note: These setup instructions were written with local ruby version `2.6.0`. For the following instructions, prepend `sudo` to the commands as needed.

Install the bundler:
```commandline
gem install bundler
```

If there are any complaints from ruby, install the version it recommends by specifying the version.

```commandline
gem install bundler -v 2.4.22
```

The next step should be to `bundle install`, however in the current dependencies, there's a [known issue](https://stackoverflow.com/a/73042570). Find the version of ffi from the `GEMFILE.lock` and attempt to install it with the following flags:

```commandline
gem install ffi -v '1.12.2' -- --with-cflags=-Wno-implicit-function-declaration
```

From here, you should be able to run the following command to download the rest of the dependencies. This command will use the `GEMFILE.lock` to resolve dependencies:

```
bundle install
```

Finally, run the command to bring the local site up:

```commandline
bundle exec jekyll serve
```

The `jekyll serve` command serves up a local instance of the site on port 4000.
Visit the instance in your browser at localhost:4000. If you need more in-depth
instructions, check out [jekyll's website](https://jekyllrb.com).

## Process

Please do not push straight to master. For now, let's try to do all work on branches
unless you have been approved to push straight to master. Make a PR if you want to
make a change, and if it is approved, it will be merged in to the site. This will
hopefully keep the website clean and functional. 

