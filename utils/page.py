import numpy as np

def page(items,current_page, num_one_page):
    """
    :param items:   数据库查询得出的query set 对象
    :param current_page: 当前页
    :param num_one_page:  每一页的 item 数目
    :return:  下一页的详细信息字典，包括上一页 ，当前页，下一页，分页信息，下一页item
    """
    num_items = len(items)        # 总的 item 数量
    num_page = num_items // num_one_page if (num_items % num_one_page) == 0 else (num_items // num_one_page) + 1  # 总的页数
    current_page = current_page if current_page <= num_page else num_page

    start = (current_page -1) * num_one_page
    end = current_page * num_one_page if (current_page * num_one_page) <= num_items else num_items
    page_item = items[start:end]    # 当前页的 item

    shang = current_page // 5 if (current_page % 5) != 0 else (current_page // 5) - 1
    temp = num_page if (shang + 1) * 5 > num_page else (shang +1) * 5
    page_list = [i for i in range(shang * 5 + 1, temp + 1)]
    previous_page = current_page - 1 if current_page != 1 else 1
    next_page = 1 if current_page >= num_page else (current_page + 1)

    next_page_info = {
        "previous_page": previous_page,
        "current_page": current_page,
        "next_page": next_page,
        "page_list": page_list,
        "page_item": page_item,
    }
    return next_page_info

if __name__ =="__main__":
    items = [i for i in range(0, 102)]
    next_page_info = page(items, 11, 10)
    print("previous_page:", next_page_info["previous_page"])
    print("current_page:", next_page_info["current_page"])
    print("next_page:", next_page_info["next_page"])
    print("page_list:", next_page_info["page_list"])
    print("page_item:", next_page_info["page_item"])


