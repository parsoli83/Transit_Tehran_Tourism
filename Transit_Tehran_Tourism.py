from fpdf import FPDF
import argparse
import json


def main():
    args=get_input()
    l = trip_metro(trip_list(args))
    if args.generate=="pdf":
        catalog_pdf(l)
    elif args.generate=="ascii":
        catalog_ascii(l)
    elif args.generate=="text":
        catalog_text(l)
    


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g",
        "--generate",
        type=str,
        help="generates a trip advisory catalog",
        default="text",
        choices=["text", "ascii", "pdf", "gif"],
    )
    parser.add_argument(
        "-n",
        type=int,
        help="number of attractions you want to see",
        default=4,
        choices=range(1, 14),
    )
    parser.add_argument(
        "-historical",
        help="if you want to see historical attractions",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-green",
        help="if you want to see green attractions",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-restaurant",
        help="if you want to see restaurants",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-recreational",
        help="if you want to see recreational attractions",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    return args


def trip_list(args):
    with open("attractions.json") as attractions_json:
        attractions = json.load(attractions_json)
        l = []
        for attraction in attractions:
            l.append(
                [
                    attraction,
                    attractions[attraction]["access"],
                    attractions[attraction]["line"],
                ]
            )
            if len(l) == args.n:
                break
        return l


def trip_metro(l):
    final = []
    for i in range(len(l) - 1):
        if l[i][1] == l[i + 1][1]:
            final.append([l[i][0], l[i][1], 0])
        else:
            cross = metro([l[i][1], l[i][2]], [l[i + 1][1], l[i + 1][2]])
            if cross == False:
                final.append([l[i][0], l[i][1], 1])
            else:
                final.append([l[i][0], l[i][1], cross])
    final.append([l[-1][0], l[-1][1], 2])
    return final
    # 0 the same
    # 1 same line
    # 2 end of the trip
    # string cross


def metro(s_stn, e_stn):
    l_crossings = {
        "14": "Darvazeh Dolat",
        "17": "Mohammadieh",
        "16": "Haft e Tir",
        "47": "Towhid",
        "46": "Meydan-e Shohada",
        "76": "Daneshgah-e Tarbiat Modarres",
        "41": "Darvazeh Dolat",
        "71": "Mohammadieh",
        "61": "Haft e Tir",
        "74": "Towhid",
        "64": "Meydan-e Shohada",
        "67": "Daneshgah-e Tarbiat Modarres",
    }
    cross = False
    try:
        if s_stn[0] != e_stn[0]:
            cross = l_crossings[f"{s_stn[1]}{e_stn[1]}"]
        return cross
    except:
        return cross


def catalog_pdf(l):
    page = FPDF(orientation="P", format="A4")
    for i in range(len(l) - 1):
        page.add_page()
        page.set_font("helvetica", "B", 20)
        page.cell(txt=f"{i+1}: {l[i][0]}", align="C", center=True, ln=2)
        page.cell(txt=f"metro: {l[i][1]}", align="C", center=True, ln=2)
        page.cell(txt=f".", align="C", center=True, ln=2)
        if l[i][2] == 0:
            page.cell(
                txt=f"next attraction is in the same station!",
                align="C",
                center=True,
                ln=2,
            )
        elif l[i][2] == 1:
            page.cell(
                txt=f"next attraction is on the same line!",
                align="C",
                center=True,
                ln=2,
            )
            page.cell(txt=f"next station: {l[i+1][1]}", align="C", center=True, ln=2)
        elif l[i][2] == 2:
            page.cell(txt=f"end of the trip!", align="C", center=True, ln=2)
        else:
            if l[i + 1][2] == 2:
                page.cell(txt=f"end of the trip!", align="C", center=True, ln=2)
                page.image(f"images/{l[i][0]}.jpg", x=10, y=80, w=190)
                break
            page.cell(
                txt=f"go to {l[i][2]} and change line", align="C", center=True, ln=2
            )
            page.cell(txt=f"next station: {l[i+1][1]}", align="C", center=True, ln=2)
        page.image(f"{l[i][0]}.jpg", x=10, y=80, w=190)
    page.output("catalog_pdf.pdf")


def catalog_ascii(l):
    print(l)
    for i in range(len(l) - 1):
        print("########################################")
        print(f"{i+1}: {l[i][0]}")
        print(f"metro: {l[i][1]}")
        print("***")
        if l[i][2] == 0:
            print(f"next attraction is in the same station!")
        elif l[i][2] == 1:
            print(f"next attraction is on the same line!")
            print(f"next station: {l[i+1][1]}")
        elif l[i][2] == 2:
            print(f"end of the trip!")
        else:
            if l[i + 1][2] == 2:
                print(f"end of the trip!")
                break
            print(f"go to {l[i][2]} and change line")
            print(f"next station: {l[i+1][1]}")
    return 0


def catalog_text(l):
    for i in range(len(l) - 1):
        print(f"{i+1}: {l[i][0]}")
        print(f"metro: {l[i][1]}")
        if l[i][2] == 0:
            print(f"next attraction is in the same station!")
        elif l[i][2] == 1:
            print(f"next attraction is on the same line!")
            print(f"next station: {l[i+1][1]}")
        elif l[i][2] == 2:
            print(f"end of the trip!")
        else:
            if l[i + 1][2] == 2:
                print(f"end of the trip!")
                break
            print(f"go to {l[i][2]} and change line")
            print(f"next station: {l[i+1][1]}")
    return 0


if __name__ == "__main__":
    main()
