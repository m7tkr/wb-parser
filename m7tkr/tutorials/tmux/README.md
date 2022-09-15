# TMUX shortcuts

* [form shell] `tmux new -s<session-name>` : create new SESSION w/ name specified
* `tmux new '<shell script>` or `tmux new -- <shell script>` : new session w/ bash script to run in it
* [form tmux] `tmux new -n<name-new-window>` : new WINDOW w/ name specified
* `tmux new -n<window-name> top` : new window running top
* `exit` : close active window

* `C-b ?` : list keys binding
* `C-b c` : new window
* `C-b :` : tmux command prompt
* `;` : separates commands in command prompt
* `C-b d` : detach from session
* `tmux attach -t<session-name>` : attach to session w/ name
* `tmux attach -dt<session-name>` : attach to session w/ name and detach other clients
* `tmux attach new -As<session-name>` : attach if exists, else create and attach
* `tmux ls` : list sessions that can be attached to
* `:kill-server` : kills server if no active session

* `:new-window -d` : new window, but doesn't make it current
* `:new-window -n<window-name>` : new name window
* `:neww -t<index>` : new window w/ specified index
* `:neww top` : new window running top

## change windows

* `:split-window` : splits window
* `C-b %` : horizontal split
* `C-b "` : vertical split
* `tmux splitw -h/-v` : horiz/vert split
* `tmux splitw -f` : span new panned accross window height and width, no constarints
* `tmux splitw -b` : new window placed left/above
* `C-b <0-9>` : change current window <number>
* `C-b '` : prompts for a window index and changes to that window
* `C-b n/p/l` : change current window to next/previous/last

## change pane

* `C-b q` : prints pane number; press <number> while active = change pane
* `C-b o` : moves to next pane
* `C-b C-o` : swaps w/ active pane

## choose session/windows/panes (tree mode)

* `C-b s` : shows sessions
* `C-b w` : shows sessions expanded w/ active window
* `C-b t/T` : tag/untagg item in tree mode
* `X` : kill all tagged items in tree mode
* `:` : prompt for all tagged items in tree mode 
* `:choose-tree` : active tree

## detach other clientall tagged items in tree modes

> read later

## killing window/session/pane

`C-b &` : kills current window w/ all panes in it; bound to `kill-window` 
`C-b x` : kills active pane; bound to `kill-pane`
`:kill-server` : kills attached session w/ all its windows

## renaming sessions/windows

`C-b $` : prompt to rename current sesssion; bound to `rename-session`
`C-b ,` : prompt to rename current window; bound to `rename-window`

## swapping panes

`C-b m` : toggles selection of current pane
`C-b M` : deselects current pane
`M` : marked pane take this symbol
`swap-pane` : swap selected pane
`C-b {` or `C-b }` : swap selected pane
`:move-window`, `C-b .` : prompt for an new index of current window
`:move-window -kt999` : `-k` replace w/ current window, if window exist in desired
`:movew -r` : restructure windows indexes

## resizing panes

`C-b z` : make current pane take all height/width; back toggling
`C-b l/r/d/u` : small step resize pane
`C-b M-l/r/d/u` : large step resize pane

## changing pane layout

`C-b <Space>` : moving through predefined pane layouts
`C-b M-1/2/3/4/5` : switch to available pane layouts

## copying text

> piece of copied called a paste buffer
>
> copied text inserted into buffers up to 50
>
> read about renameing buffers

`C-b [` : enter copy mode
`C-b ]` : paste recently copied text
`C-b =` : enter buffer mode
`C-b p/P` : paste selected/tagged buffer(s)
`C-b d/D` : delete selected/tagged buffer(s)

## finding windows and panes

`C-b f` : acts like `grep` on visible content; gives tree as result

## using mouse 

> no need in it

- - -

* https://github.com/tmux/tmux/wiki/Getting-Started - Getting Started w/ tmux
