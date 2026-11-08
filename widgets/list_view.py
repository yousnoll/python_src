import cProfile
import random
import time
import tkinter as tk
from dataclasses import dataclass, field
from tkinter import ttk
from typing import Any

# TODO: row_id = iid を使って管理するのは確定
# データとしての挿入順は絶対に維持しなければならない。

# TODO: immutable にして、完全に外とのやり取り用とかがいいのかな
# 中は dict で管理でいいんじゃね？

# TODO: そういや、ソートやフィルターを適用するだけなら、iid のあれこれすればいいんじゃね？
# 1000 件程度だと一瞬だな
# マシンスペックか？それとも単純だからか？あるいは Python 事態？

# 10000 件あっても、時間的には一瞬なんだな
# ただそれでも、明確に差があるな
# ちゃんと、測らないとダメかな
# full_reload: 0.028150558471679688 sec
# full_reload: 0.02835702896118164 sec
# full_reload: 0.028143882751464844 sec
# detach_and_reattach: 0.006705284118652344 sec
# detach_and_reattach: 0.006808280944824219 sec
# detach_and_reattach: 0.006970643997192383 sec

@dataclass
class DataRow:
    checked: bool = False

# TODO: insert で指定した image はどこに表示ｓれるのか？
# #0 と呼ばれる列？
# それとも純粋に左端なんだろうか？
# #0 所謂、ツリー列に表示されるので、show="heading"だと表示されない。
# また displaycolumns の影響を受けなず、並び替えも効かず、常に表示される。



class ListView(ttk.Frame):
    def __init__(self, master = None, image = None, **kw):
        super().__init__(master, **kw)

        self._iids: list[str] = []
        self._values_by_iid: dict[str, tuple[Any, ...]] = {}

        columns = [f"col{i + 1}" for i in range(3)]

        self._treeview = ttk.Treeview(self, columns=columns, show="headings")
        # self._treeview = ttk.Treeview(self, columns=columns)
        self._treeview.heading('#0', text='Image')
        self._treeview.pack(expand=True, fill="both")

        self._image = image

        for col in columns:
            self._treeview.heading(col, text=col)

        self._treeview.bind("<Button-1>", self._on_button_1)

    def insert_test_data(self, count: int = 10000):

        # image = tk.PhotoImage(file="C:\\tmp\\家のアイコン素材.png")

        for i in range(count):
            values = (
                f"Item-{i}",
                random.randint(0, 100),
                f"C{i}-2"
            )

            iid = self._treeview.insert(
                "",          # 固定
                iid=None,    # 中で管理するか、外から指定できるべきか？
                index="end", # 挿入位置だから、外から指定できるべき
                image=self._image,
                values=values
            )

            self._iids.append(iid)
            self._values_by_iid[iid] = values

        print(self._iids[-1])


    def insert_test_data2(self):
        for i in range(10):
            values = (
                f"Item-{i}",
                random.randint(0, 100),
                None
            )

            iid = self._treeview.insert(
                "",          # 固定
                iid=None,    # 中で管理するか、外から指定できるべきか？
                index="end", # 挿入位置だから、外から指定できるべき
                values=values
            )

            print(iid)
    def insert_test_error(self):
        # TODO: 恐らく iid=None のときカウントが増える？

        values = (
            "Item-0",
            random.randint(0, 100),
            "C0-2"
        )

        iid = self._treeview.insert(
            "",
            iid="I002", # 自動生成せず、故意に重複するものを追加すると？
            index="end",
            values=values
        )

        iid = self._treeview.insert(
            "",          # 固定
            iid=None,    # 中で管理するか、外から指定できるべきか？
            index="end", # 挿入位置だから、外から指定できるべき
            values=values
        )

        print(iid)
        

    def delete_all(self):
        print("delete_all")
        iids = self._treeview.get_children()
        self._treeview.delete(*iids)

    def full_reload(self):
        start = time.time()

        iids = self._treeview.get_children()
        self._treeview.delete(*iids)

        for iid in self._iids:
            values = self._values_by_iid.get(iid)
            iid = self._treeview.insert("", index="end",iid=iid, values=values)

        t = time.time() - start
        print(f"full_reload: {t:.3f} sec")

    def detach_and_reattach(self):
        start = time.time()

        iids = self._treeview.get_children()
        self._treeview.detach(*iids)

        # detachしたものは取得できない
        # 自分で管理しないとダメらしい
        # iids2 = self._treeview.get_children()
    
        for iid in iids:
            self._treeview.reattach(iid, "", index="end")

        t = time.time() - start
        print(f"detach_and_reattach: {t:.3f} sec")
    

    def insert(self):
        
        pass

    def refresh(self):
        # TODO: ここでフィルターとソートした結果に基づき、得た id を使い
        #       detach  + reattach or move するのが正解？
        # TODO: 元々ソートってどうやってたんだっけ？
        pass

    
    

    def _on_button_1(self, event: tk.Event):
        print("----- _on_button_1 -----")
        print(event)
        print(event.type)
        # この環境だとヘッダーの硬さは 24 か？


        # identify_region という、ズバリがあるじゃん
        region = self._treeview.identify_region(event.x, event.y)
        print(f"region={region}")
