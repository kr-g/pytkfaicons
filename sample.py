import tkinter as tk

from pytkfaicons.conv import build, convert_all, copy_meta


# build(opts="-c", callb=print)


from pytkfaicons.icons import read_icons, get_icon_image, tk_image_loader, get_tk_icon
from pytkfaicons.icons import get_scaled_tk_icon

read_icons()


root = tk.Tk()

frame1 = tk.Frame(root)
tk.Label(frame1, text="on the fly resized (slow)").pack(side="left")

# resize on the fly (slow)
img0 = get_scaled_tk_icon("arrow-left", "solid", 64)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img0).pack(side="left")

img1 = get_scaled_tk_icon("arrow-right", "solid", 48)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img1).pack(side="left")

img2 = get_scaled_tk_icon("asterisk", "solid", 32)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img2).pack(side="left")

img3 = get_scaled_tk_icon("barcode", "solid", 24)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img3).pack(side="left")

img4 = get_scaled_tk_icon("baby", "solid", 12)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img4).pack(side="left")

img5 = get_scaled_tk_icon("bahai", "solid", 8)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img5).pack(side="left")

img6 = get_scaled_tk_icon("bars", "solid", 6)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img6).pack(side="left")

frame1.pack()

# this is the same implementation as get_tk_icon()
# using get_icon_image(), and tk_image_loader() as loader
# what returns tk.PhotoImage


def icon(name, style):
    # pre-calculated 32px height icons (fast)
    return get_icon_image(name, style, loader=tk_image_loader)


frame2 = tk.Frame(root)

left = icon("arrow-left", "solid")
right = icon("arrow-right", "solid")
asterisk = icon("asterisk", "solid")
barcode = icon("barcode", "solid")
baby = icon("baby", "solid")
bahai = icon("bahai", "solid")
bars = icon("bars", "solid")

tk.Label(frame2, text="pre-caclulated (fast)").pack(side="left")

tk.Button(frame2, justify=tk.LEFT, padx=10, image=left).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=right).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=asterisk).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=barcode).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=baby).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bahai).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bars).pack(side="left")

frame2.pack()

root.mainloop()
