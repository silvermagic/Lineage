//
// Created by 范炜东 on 2018/12/11.
//

#ifndef LINEAGE_ITEM_H
#define LINEAGE_ITEM_H

namespace Lineage {

class Item {
public:

    double weight();

    virtual std::string name();

public:
    int enchant_level;
    int count;
    bool bless;
    int attr_enchant_kind;
    int attr_enchant_level;
};

}

#endif //LINEAGE_ITEM_H
