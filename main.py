"""在终端添加和查看阅读记录。运行：python3 main.py"""


def main():
    records = []

    while True:
        print("\n我的阅读记录")
        print("1. 添加记录")
        print("2. 查看记录")
        print("3. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            title = input("书名：").strip()
            if not title:
                print("书名不能为空。")
                continue
            note = input("一句读后感：").strip()
            records.append({"title": title, "note": note})
            print("添加成功！")

        elif choice == "2":
            if not records:
                print("目前还没有记录。")
            for number, record in enumerate(records, start=1):
                print(f"\n{number}. {record['title']}")
                print(f"   读后感：{record['note']}")

        elif choice == "3":
            print("下次见！")
            break

        else:
            print("请输入 1、2 或 3。")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n下次见！")
