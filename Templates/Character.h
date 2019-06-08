//
// Created by 范炜东 on 2019/5/10.
//

#ifndef PROJECT_DB_DEF_CHARACTER_H
#define PROJECT_DB_DEF_CHARACTER_H

#include <memory>
#include <string>
#include <ctime>

namespace db {
namespace def {

class Character : public std::enable_shared_from_this<Character> {
public:
  int access_level();
  virtual void access_level(int);
  int max_hp();
  void max_hp(int);
  int cur_hp();
  void cur_hp(int);
  int max_mp();
  void max_mp(int);
  int cur_mp();
  void cur_mp(int);
  int ac();
  void ac(int);
  int str();
  void str(int);
  int dex();
  void dex(int);
  int con();
  void con(int);
  int men();
  void men(int);
  int wis();
  void wis(int);
  int cha();
  void cha(int);
  int face();
  void face(int);
  int justice();
  void justice(int);

public:
  int id; // 编号
  std::string account_name; // 账户名称
  std::string character_name; // 角色名称
  int metempsychosis; // 转生次数
  int level; // 等级
  int high_level; // 转身/死亡前最高等级
  int exp; // 经验值
  int status; // 状态（死亡、行走、空闲等）
  int career; // 职业
  bool sex; // 性别
  int x; // X轴坐标
  int y; // Y轴坐标
  int map_id; // 地图编号
  int food; // 饱食度
  std::string title; // 封号
  int clan_id; // 血盟编号
  std::string clan_name; // 血盟名称
  int clan_class; // 血盟阶级
  int bonus_status; // 升级奖励的属性点状态
  int elixir_status; // 万能药水奖励的属性点状态
  int elf_attr; // 精灵属性（风、火、土、水）
  int exp_rec; // 经验恢复
  int partner_id; // 伴侣
  bool online_status; // 在线状态
  int hometown_id; // 村庄编号
  int contribution; // 村庄贡献度
  int pay;
  int hell_stay_time; // 地狱停留时间
  bool banned; // 禁用
  int karma; // 业障（友好度）
  int pk_count; // pk次数（用于警卫攻击判定）
  int pk_count_for_elf; // pk次数（用于精灵守卫攻击判定）
  std::tm last_pk; // 最近决斗时间
  std::tm last_pk_for_elf; // 最近决斗时间
  std::tm deadline; // 角色删除日期
  int original_str; // 初始力量
  int original_dex; // 初始敏捷
  int original_con; // 初始体质
  int original_men; // 初始精神
  int original_wis; // 初始智力
  int original_cha; // 初始魅力
  std::tm last_active; // 角色登出时间（殷海萨的祝福计算时间）
  int ain_zone; // 殷海萨的祝福区域
  int ain_point; // 殷海萨的祝福值
  int honor; //
  int kills;
  std::tm birthday; // 角色创建日期

protected:
  int access_level_; // 角色权限（GM、监控、普通）
  int max_hp_; // 最大体力值 => Health Point
  int cur_hp_; // 当前体力值
  int max_mp_; // 最大魔力值 => Magic Point
  int cur_mp_; // 当前魔力值
  int ac_; // 防御值(值越小代表防御越高) => Armor Class
  int str_; // 力量属性 => Strength
  int dex_; // 敏捷属性 => Dexterity
  int con_; // 体质属性 => Constitution
  int men_; // 精神属性 => mentality
  int wis_; // 智力属性 => Wisdom
  int cha_; // 魅力属性 => Charming
  int face_; // 朝向
  int justice_; // 正义值
};

}
}

#endif //PROJECT_DB_DEF_CHARACTER_H
