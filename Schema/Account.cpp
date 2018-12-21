//
// Created by 范炜东 on 2018/11/25.
//

#include "Storage.h"
#include "Account.h"

namespace Lineage {

Account::Account(std::string name) : name_(name), is_valid_(false), access_level_(0) {
}

bool Account::isGM() {
    return access_level_ > 0;
}

bool Account::validatePassword(std::string pwd) {
    is_valid_ = password_ == pwd;
    return is_valid_;
}

std::string Account::name() {
    return name_;
}

bool Account::load() {
    Session ses(Storage::getSingleton().get());
    ses << "SELECT password, lastactive, access_level, ip, host, banned, character_slot FROM accounts WHERE login=?",
            into(password_), into(last_active), into(access_level_), into(ip), into(host), into(banned), into(
            character_slot), use(name_), now;
    return true;
}

int Account::countCharacters() {
    Session ses(Storage::getSingleton().get());
    int count;
    ses << "SELECT count(*) as cnt FROM characters WHERE account_name=?", into(count), use(name_), now;
    return count;
}

bool Account::exist() {
    Session ses(Storage::getSingleton().get());
    int count;
    ses << "SELECT count(*) FROM accounts WHERE login=? LIMIT 1", into(count), now;
    if (count == 1)
        return true;
    else
        return false;
}

bool Account::save() {
    Session ses(Storage::getSingleton().get());
    ses << "INSERT INTO accounts SET VALUES(?, ?, ?, ?, ?, ?, ?)", use(name_), use(password_), use(access_level_), use(ip), use(host), use(banned), use(character_slot), now;
    return true;
}

bool Account::updateBanned() {
    Session ses(Storage::getSingleton().get());
    ses << "UPDATE accounts SET banned=? WHERE login=?", use(banned), use(name_), now;
    return true;
}

bool Account::updateCharacterSlot() {
    Session ses(Storage::getSingleton().get());
    ses << "UPDATE accounts SET character_slot=? WHERE login=?", use(character_slot), use(name_), now;
    return true;
}

bool Account::updateLastActive() {
    Session ses(Storage::getSingleton().get());
    ses << "UPDATE accounts SET lastactive=?, ip=?, host=? WHERE login = ?", use(last_active), use(ip), use(host), use(name_), now;
    return true;
}

}