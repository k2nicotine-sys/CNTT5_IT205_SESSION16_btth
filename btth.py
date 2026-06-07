blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]


def find_blood_index(inventory, blood_id):
    """
    Tìm vị trí túi máu theo mã.
    Trả về index nếu tìm thấy, ngược lại trả về -1.
    """
    blood_id = blood_id.strip().upper()

    for index in range(len(inventory)):
        info = inventory[index].split("-")

        if info[0] == blood_id:
            return index

    return -1


def display_inventory(inventory):
    """
    Hiển thị danh sách túi máu và tổng thể tích.
    """
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print("\n--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("--------------------------------------------------------------")

    total_volume = 0

    for item in inventory:
        info = item.split("-")

        blood_id = info[0]
        donor_name = info[1]
        blood_group = info[2]
        volume = int(info[3])
        expiry_date = info[4]

        total_volume += volume

        print(
            f"{blood_id:<6} | "
            f"{donor_name:<16} | "
            f"{blood_group:<8} | "
            f"{volume} ml".ljust(8) + " | "
            f"{expiry_date}"
        )

    print("--------------------------------------------------------------")
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    """
    Thêm túi máu mới vào kho.
    """
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_id = input("Nhập mã túi máu mới: ").strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    if find_blood_index(inventory, blood_id) != -1:
        print(f"\nLỗi: Mã túi máu {blood_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor_name = " ".join(
        input("Nhập tên người hiến: ").split()
    ).title()

    if donor_name == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_group = input("Nhập nhóm máu: ").strip().upper()

    try:
        volume = int(input("Nhập thể tích (ml): "))

        if volume <= 0:
            print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
            return

    except ValueError:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry_date = input(
        "Nhập ngày hết hạn (DD/MM/YYYY): "
    ).strip()

    blood_info = [
        blood_id,
        donor_name,
        blood_group,
        str(volume),
        expiry_date
    ]

    new_blood_bag = "-".join(blood_info)

    inventory.append(new_blood_bag)

    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")
    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_blood_bag)


def update_expiry(inventory):
    """
    Gia hạn hoặc sửa ngày hết hạn.
    Thể hiện tính bất biến của String:
    split -> sửa -> join -> ghi đè.
    """
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_id = input(
        "Nhập mã túi máu cần cập nhật: "
    ).strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    new_expiry = input(
        "Nhập ngày hết hạn mới: "
    ).strip()

    # String là immutable -> phải split rồi join lại
    info = inventory[index].split("-")

    info[4] = new_expiry

    inventory[index] = "-".join(info)

    print(
        f"\nThành công: Đã cập nhật ngày hết hạn "
        f"cho túi máu {blood_id}!"
    )


def remove_blood_bag(inventory):
    """
    Xuất hoặc hủy túi máu khỏi kho.
    """
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_id = input(
        "Nhập mã túi máu cần xuất/hủy: "
    ).strip().upper()

    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    inventory.pop(index)

    print(
        f"\nThành công: Đã xuất túi máu "
        f"{blood_id} khỏi kho!"
    )


def display_menu():
    """
    Hiển thị menu hệ thống.
    """
    print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
    print("1. Xem danh sách túi máu trong kho")
    print("2. Nhập túi máu mới")
    print("3. Gia hạn / Sửa ngày hết hạn")
    print("4. Xuất / Hủy túi máu")
    print("5. Thoát chương trình")
    print("========================================")


def main():
    """
    Hàm điều hướng chương trình.
    """
    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        ).strip()

        match choice:
            case "1":
                display_inventory(blood_inventory)

            case "2":
                add_blood_bag(blood_inventory)

            case "3":
                update_expiry(blood_inventory)

            case "4":
                remove_blood_bag(blood_inventory)

            case "5":
                print(
                    "Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ, "
                    "vui lòng nhập số từ 1-5!"
                )


main()