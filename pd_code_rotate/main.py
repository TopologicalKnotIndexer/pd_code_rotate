import pd_code_sanity
import pd_code_pre_nxt

def rotate(pd_code:list[list]) -> list[list]:

    # 检查是不是合法的 pd_code
    if not pd_code_sanity.sanity(pd_code):
        raise ValueError()
    
    # 获得前驱后继
    _, nxt = pd_code_pre_nxt.get_pre_nxt(pd_code)

    new_pd_code = []
    for crossing in pd_code: # 对所有 crossing 进行翻面
        ax, bx, cx, dx = crossing
        if nxt[bx] == dx:
            new_pd_code.append([bx, ax, dx, cx])
        else:
            new_pd_code.append([dx, cx, bx, ax])
    
    return new_pd_code

if __name__ == "__main__":
    print(rotate([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))
