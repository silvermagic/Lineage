//
// Created by 范炜东 on 2018/11/25.
//

#ifndef LINEAGE_ACCOUNT_H
#define LINEAGE_ACCOUNT_H

#include <Poco/DateTime.h>

namespace Lineage {

using Poco::DateTime;

class Account {
public:
    Account(std::string name);

    /* 是否是管理员权限 */
    bool isGM();
    /* 校验密码是否正确 */
    bool validatePassword(std::string pwd);

    /* 属性存取 */
    std::string name();

    /* 加载数据库 */
    bool load();
    /* 查询数据库 */
    bool exist();
    int countCharacters();
    /* 插入数据库 */
    bool save();
    /* 更新数据库 */
    bool updateBanned();
    bool updateCharacterSlot();
    bool updateLastActive();

protected:
    //static std::string encodePassword(std::string raw);

public:
    bool banned; // 账户是否已经被禁用
    int character_slot; // 账户角色个数
    std::string ip, host; // 账户登入地址
    DateTime last_active; // 账户最近登入时间

protected:
    bool is_valid_; // 账户是否已经通过验证
    int access_level_; // 账户权限等级
    std::string name_; // 账户名称
    std::string password_; // 账户密码
};

}

#endif //LINEAGE_ACCOUNT_H
