
seznam = []

html_file = "veganisonevarni2py.html"
to_write = open("veganisonevarni.html", "wt")

with open(html_file, "rt") as src:
    for vrstica in src:
        to_write.write(vrstica)
        if vrstica.strip() == "<!-- add_content -->":
            with(open("./ljudje/links", "rt")) as f:
                rows = list(f)
                num_rows = len(rows)
                html2insert = """<div class="item">
                <p class="ime_c"><b>Število korenjakov: <span class="colorText">{0}</span></b></p>
                </div>
                """.format(num_rows)
                to_write.write(html2insert)
                for row in rows:
                    ime_t, povezava_t = row.split(" ")

                    slika = ime_t+".png"
                    ime = " ".join(ime_t.split("_"))
                    povezava = povezava_t.strip()
                    html2insert = """<div class="item">
                                    <p class="ime_c"><b><span class="colorText">Korenjak: </span></b> <a class = "{0}" href="{2}">{0}</a></p>
                                    <img src="./ljudje/{1}" alt="{0}"/>
                                    </div>
                                    """.format(ime, slika, povezava)
                    to_write.write(html2insert)

to_write.close()