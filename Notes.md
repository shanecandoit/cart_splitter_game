
# Notes - Development

Switches are 2x2 blocks

    |?
    |-

Tracks are 1x2 blocks. So they are on alternating rows/cols.

    ║.║
    ║.║


horizontal

    ==
    ..
    ==

Use pygame or maybe text ui <https://textual.textualize.io/> ?

How to wrap text in pygame (for UI): <https://www.pygame.org/wiki/TextWrap>

## Colors

<https://colorhunt.co/palette/2b2a4cb31312ea906ceee2de>

    navy    # 2b2a4c    rgb(43, 42, 76)
    red     # b31312    rgb(179, 19, 18)
    orange  # ea906C    rgb(234, 144, 108)
    peach   # eee2de    rgb(238, 226, 222)

## Drawing Chars

    ║ ver
    ═ or = hor
    ╠ switch
    ↓ v down
    → > right

## State Machine Code

- Given "abcXdefYghi"
- Say we want to collect from X until Y, like:
- Bucket1 down: abc ghi
- Bucket2 right: XdefY

With row: `| S1 | e1 | S2 |`

When we are facing (in state) S1, and if we get E1, then goto S2

| when | if | then |
|------|----|------|
| v    | X  | >    |
| >    | Y  | v    |
