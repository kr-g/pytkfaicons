import tkinter as tk

from pytkfaicons.conv import build


# build(opts="-c", callb=print)


from pytkfaicons.icons import read_icons, get_icon_image, tk_image_loader, get_tk_icon

read_icons()

root = tk.Tk()


# this is the same implementation as get_tk_icon()
# using get_icon_image(), and tk_image_loader() as loader
# what returns tk.PhotoImage


def icon(name, style):
    return get_icon_image(name, style, loader=tk_image_loader)


left = icon(
    "arrow-left",
    "solid",
)

right = icon(
    "arrow-right",
    "solid",
)

asterisk = icon(
    "asterisk",
    "solid",
)

barcode = icon(
    "barcode",
    "solid",
)

baby = icon(
    "baby",
    "solid",
)

bahai = icon(
    "bahai",
    "solid",
)

bars = icon(
    "bars",
    "solid",
)


tk.Button(root, justify=tk.LEFT, padx=10, image=left).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=right).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=asterisk).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=barcode).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=baby).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=bahai).pack(side="left")
tk.Button(root, justify=tk.LEFT, padx=10, image=bars).pack(side="left")

root.mainloop()
