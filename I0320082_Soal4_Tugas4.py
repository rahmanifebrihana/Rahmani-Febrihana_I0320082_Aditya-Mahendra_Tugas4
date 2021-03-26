usia = 21
p = int(input("Berapa usia anda : "))
if usia <= p :
    print("Anda memenuhi usia")
    q = str(input("Apakah anda lulus ujian kualifikasi (Y/T) "))
    if q == "Y" :
        print("Anda boleh mengikuti kursus")
    elif q == "T" :
        print("Anda tidak boleh mengikuti kursus")

else :
    print("Anda tidak memenuhi usia")

