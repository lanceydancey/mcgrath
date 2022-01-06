# Using `git`

- [Quick guide to git](http://rogerdudler.github.io/git-guide/)
- [Challenge based approach to understanding git](https://try.github.io/levels/1/challenges/1)

--------
Git is a distributed version control system, originally created by Linus Torvalds in the spirit of BitKeeper (which was proprietary at the time). It is used to track changes to a project's source code, manage the project's history, collaborate with others, and manage releases. As Torvalds once said, he really likes naming things after himself, hence the name `git`.

At its core, the way most people use it, is as a variation on `svn`. I mention this to highlight that while git is a distributed version control system, meaning in theory there is no canonical repository, most folks do have a central repository, usually hosted on GitHub or GitLab. There's nothing wrong with this approach at all, but `git` was developed to handle the distributed nature of the Linux kernel development model -- everyone had their own repo that handled their development, then they merged with the 'blessed' repo owned by Torvalds.

These mergers are handled by what are known as *pull requests*, where a developer notifies another developer that a changed or new feature is available for them to merge into their own repo.

Some terminology:

- A repo is a source of information regarding project history and current state of code
- A branch is a logically separate lineage of code which can be merged back in to the 'master' copy (also a branch).
- To get a new copy of a git repo, you `clone` the repository to your own working space.
- You make any changes you'd like, then `commit` them to the local repo.
- At any time, you can `push` all your commits and code to another repo (called the *remote* repo)
- You can also `pull` any changes made to the remote repo and merge them in to your local copy.

One common complaint you may hear about `git` is that "you need to be a plumber in order to go to the bathroom." One of the primary goals of software development is abstraction. As a tool, I shouldn't need to know how it works internally in order to use it. Tools which require that have what is known as a *leaky abstraction*. `git` doesn't have a leaky abstraction -- that would require that it had any abstraction at all. It does not. You must be aware of, to an absurd degree, exactly how `git` works and does what it does in order to use it effectively.

At the network level, `git` supports HTTPs, HTTP, ssh, and its own protocol (the `git://` URI scheme). You do need to know which protocol a given repo is using, as you may need to deal with certificates or SSH keys.

All that said, there's some important things you'll need to know. `git` makes use of significant metadata which define a directory as a repository. Residing in the `$REPO_ROOT/.git/` directory, this metadata is:

```console
.git
├── .git/branches/          # List of branches that exist for the current repository
├── .git/COMMIT_EDITMSG     # Contains the commit message of any uncommitted, but staged content
├── .git/config             # This is the main `git` configuration file. It keeps specific `git` options for your project
├── .git/description        # It will show when you have viewed your repository or the list of all versioned repositories
├── .git/HEAD               # This file holds a reference to the branch (or commit) you currently have checked out 
├── .git/hooks/             # Directory contains shell scripts that are invoked after the corresponding `git` command
├── .git/index              # The `git` index is used as a staging area between your working directory and your repository
├── .git/info/              # Contains additional information about the repository.
├── .git/logs/              # Keeps records of changes made to refs
├── .git/objects/           # In this directory the data of your `git` objects are stored – all the contents of the files you have ever checked i
└── .git/refs/              # This directory normally contains the tips of branches and tags in  three subfolders – heads, remotes and tags
```

It is important to emphasize that `git` tracks content, not files. This means that if two files have the same content, only a single blob will exist in the `.git/objects` tree. This is also true of any identical file trees -- only a single copy of the tree will exist, with the appropriate references to recreate the tree as necessary in the cloned repository. As a corollary, empty directories can't be tracked by `git`.

Only the root of the repository will have a `.git/` folder. Any subdirectories will simply be file trees in the `.git/objects` database. The `.git/objects` database contains 4 distinct types of objects:

- blob: file data
- commit: a snapshot of the whole file system tree rooted at `$REPO_ROOT` 
- tag: specific *named* pointer to a specific commit
- tree: representation of a directory

Each commit is labeled by its SHA1 hash. A commit includes:

- The hash of the root tree 
- The hash of the parent commit(s) 
- Commit message 
- Author 
- Committer 
- Date/time of the commit 

You can have many commits to your local repo, with only a single `push`. All of the commits will be pushed to the remote repo as distinct commits, each with their own copy of the above information.

Depending on your work flow, there may be a single "blessed" repository that is managed by an individual or group, or there may be parallel internal and public repositories (with privileged information redacted from the public repo). There may also be a code review process, using something like Gerrit (a code review system which integrates with `git`).

If you have not already done so, you will need to configure your name, your email, and (at minimum) your preferred editor (this will be used for commit messages).

```console
$ git config --global user.name “Alice” 
$ git config --global user.email “alice@collab.net” 
$ git config --global core.editor code
```

Global settings apply to all repos on this host -- unless or until you define repo-specific values.

An example workflow for configuring a new repository:

```console
$ git init my-project           # initialize an empty repository
$ cp $EXTERNAL_PATH/file1 .     # add a file (with content) to file tree
$ git add file1                 # stage the new file to the index
$ git status                    # show the state of the repository, based on the index
$ git commit -m  “Add file1”    # commit all staged files, with the message "Add file1"
$ git remote add origin $URI    # add the remote repo URI to this repo
$ git push                      # push all committed changes to the remote URI
```

You can have multiple "remotes" for a given repository. If there is only one, tradition calls it `origin`. You may also have a remote called `testing` or `production` with different URIs; in this case, you need to specify the destination of `git push`.

While the above shows how to handle a newly defined repository on your local machine, you may also create it in other ways. A common example is to create a repository on the GitHub website, then clone it locally. You can make any necessary changes, then push the staged commits back to GitHub. As such:

```console
$ git clone $URI                # clone the repo found at URI
$ cp $EXTERNAL_PATH/file1 .     # add a file (with content) to file tree
$ git add file1                 # stage the new file to the index
$ git status                    # show the state of the repository, based on the index
$ git commit -m  “Add file1”    # commit all staged files, with the message "Add file1"
$ git push                      # push all committed changes to the remote URI
```

`git` is a tool with a fairly shallow learning curve when everything works as expected. Then it's a sheer cliff in the night, with an evil soul randomly throwing lubricant all over all the hand- and foot-holds.

I won't be getting into branches, rebasing, stashing, or other more complex uses of `git` often seen in a more distributed setting. See the above links for more information on these topics, or take a software engineering class which covers `git` in much more nitty gritty detail as a software development lifecycle tool.