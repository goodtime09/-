from efficient_apriori import apriori
import csv
if __name__=='__main__':
    with open('宁浩.csv','r',encoding='utf-8-sig') as f:
        lists=csv.reader(f)
        data=[]
        for names in lists:
            names_new=[]
            for name in names:
                if name.strip() != '宁浩':
                    names_new.append(name.strip())
            data.append(names_new[1:])
        print(data)
        itemset,rules = apriori(data,min_support=0.5,min_confidence=1)
        print(itemset)
        print(rules)