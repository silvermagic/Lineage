//
// Created by 范炜东 on 2019/5/13.
//

#include "ConnectionPoolManager.h"
#include "Logger.h"
#include "Templates/Character.h"
#include "Character.h"

namespace db {
namespace oper {

void Character::insert(std::shared_ptr<def::Character> role) {
  LOG_DEBUG << "Character::insert " << role->account_name << " -> " << role->character_name;
  session sql(ConnectionPoolManager::instance());
  int sex = int(role->sex);
  int online_status = int(role->online_status);
  int banned = int(role->banned);
  sql << "insert into characters (id, account_name, character_name, metempsychosis, level, high_level, access_level, exp, max_hp, cur_hp, max_mp, cur_mp, "
         "ac, str, con, dex, cha, men, wis, status, career, sex, face, x, y, map_id, food, justice, title, clan_id, clan_class, bonus_status, "
         "elixir_status, elf_attr, exp_rec, partner_id, online_status, hometown_id, contribution, pay, hell_stay_time, banned, karma, pk_count, pk_count_for_elf, "
         "last_pk, last_pk_for_elf, delete_time, original_str, original_con, original_dex, original_cha, original_men, original_wis, last_active, "
         "ain_zone, ain_point, honor, kills, birthday) values "
         "(:id, :account_name, :character_name, :metempsychosis, :level, :high_level, :access_level, :exp, :max_hp, :cur_hp, :max_mp, :cur_mp, "
         ":ac, :str, :con, :dex, :cha, :men, :wis, :status, :career, :sex, :face, :x, :y, :map_id, :food, :justice, :title, :clan_id, :clan_class, :bonus_status, "
         ":elixir_status, :elf_attr, :exp_rec, :partner_id, :online_status, :hometown_id, :contribution, :pay, :hell_stay_time, :banned, :karma, :pk_count，:pk_count_for_elf, "
         ":last_pk, :last_pk_for_elf, :deadline, :original_str, :original_con, :original_dex, :original_cha, :original_men, :original_wis, :last_active, "
         ":ain_zone, :ain_point, :honor, :kills, :birthday)",
         use(role->id), use(role->account_name), use(role->character_name), use(role->metempsychosis), use(role->level), use(role->high_level), use(role->access_level()), use(role->exp), use(role->max_hp()), use(role->cur_hp()), use(role->max_mp()), use(role->cur_mp()),
         use(role->ac()), use(role->str()), use(role->con()), use(role->dex()), use(role->cha()), use(role->men()), use(role->wis()), use(role->status), use(role->career), use(sex), use(role->face()), use(role->x), use(role->y), use(role->map_id), use(role->food), use(role->justice()), use(role->title), use(role->clan_id), use(role->clan_class), use(role->bonus_status),
         use(role->elixir_status), use(role->elf_attr), use(role->exp_rec), use(role->partner_id), use(online_status), use(role->hometown_id), use(role->contribution), use(role->pay), use(role->hell_stay_time), use(banned), use(role->karma), use(role->pk_count), use(role->pk_count_for_elf),
         use(role->last_pk), use(role->last_pk_for_elf), use(role->deadline), use(role->original_str), use(role->original_con), use(role->original_dex), use(role->original_cha), use(role->original_men), use(role->original_wis), use(role->last_active),
         use(role->ain_zone), use(role->ain_point), use(role->honor), use(role->kills), use(role->birthday);
}

std::shared_ptr<def::Character> Character::query(std::string &character_name) {
  LOG_DEBUG << "Character::query " << character_name;
  std::shared_ptr<def::Character> role = nullptr;
  row r;
  session sql(ConnectionPoolManager::instance());
  sql << "select id, account_name, character_name, metempsychosis, level, high_level, access_level, exp, max_hp, cur_hp, max_mp, cur_mp, "
        "ac, str, con, dex, cha, men, wis, status, career, sex, face, x, y, map_id, food, justice, title, clan_id, clan_class, bonus_status, "
        "elixir_status, elf_attr, exp_rec, partner_id, online_status, hometown_id, contribution, pay, hell_stay_time, banned, karma, pk_count, pk_count_for_elf, "
        "last_pk, last_pk_for_elf, deadline, original_str, original_con, original_dex, original_cha, original_men, original_wis, last_active, "
        "ain_zone, ain_point, honor, kills, birthday from characters where character_name = :character_name", use(character_name), into(r);
  if (sql.got_data()) {
    int access_level, max_hp, cur_hp, max_mp, cur_mp, ac, str, con, dex, cha, men, wis, sex, face, justice, online_status, banned;
    role = std::make_shared<def::Character>();
    r >> role->id >> role->account_name >> role->character_name >> role->metempsychosis >> role->level
      >> role->high_level >> access_level >> role->exp >> max_hp >> cur_hp >> max_mp >> cur_mp
      >> ac >> str >> con >> dex >> cha >> men >> wis >> role->status >> role->career >> sex >> face
      >> role->x >> role->y >> role->map_id >> role->food >> justice >> role->title >> role->clan_id
      >> role->clan_class >> role->bonus_status >> role->elixir_status >> role->elf_attr >> role->exp_rec >> role->partner_id
      >> online_status >> role->hometown_id >> role->contribution >> role->pay >> role->hell_stay_time >> banned
      >> role->karma >> role->pk_count >> role->pk_count_for_elf >> role->last_pk >> role->last_pk_for_elf >> role->deadline
      >> role->original_str >> role->original_con >> role->original_dex >> role->original_cha >> role->original_men >> role->original_wis
      >> role->last_active >> role->ain_zone >> role->ain_point >> role->honor >> role->kills >> role->birthday;
    role->access_level(access_level);
    role->max_hp(max_hp);
    role->cur_hp(cur_hp);
    role->max_mp(max_mp);
    role->cur_mp(cur_mp);
    role->ac(ac);
    role->str(str);
    role->con(con);
    role->dex(dex);
    role->cha(cha);
    role->men(men);
    role->wis(wis);
    role->sex = (sex != 0);
    role->face(face);
    role->justice(justice);
    role->online_status = (online_status != 0);
    role->banned = (banned != 0);
  }

  LOG_DEBUG << "Character::query " << character_name << (role != nullptr ? " success" : " failed");
  return role;
}

std::vector<std::shared_ptr<def::Character>> Character::query_by_account(std::string& account_name) {
  LOG_DEBUG << "Character::query_by_account " << account_name;
  session sql(ConnectionPoolManager::instance());
  rowset<row> rs = (sql.prepare << "select id, account_name, character_name, metempsychosis, level, high_level, access_level, exp, max_hp, cur_hp, max_mp, cur_mp, "
         "ac, str, con, dex, cha, men, wis, status, career, sex, face, x, y, map_id, food, justice, title, clan_id, clan_class, bonus_status, "
         "elixir_status, elf_attr, exp_rec, partner_id, online_status, hometown_id, contribution, pay, hell_stay_time, banned, karma, pk_count, pk_count_for_elf, "
         "last_pk, last_pk_for_elf, deadline, original_str, original_con, original_dex, original_cha, original_men, original_wis, last_active, "
         "ain_zone, ain_point, honor, kills, birthday from characters where account_name = :account_name", use(account_name));
  std::vector<std::shared_ptr<def::Character>> roles;
  for (rowset<row>::const_iterator iter = rs.begin(); iter != rs.end(); ++iter) {
    int access_level, max_hp, cur_hp, max_mp, cur_mp, ac, str, con, dex, cha, men, wis, sex, face, justice, online_status, banned;
    auto role = std::make_shared<def::Character>();
    const row &r = *iter;
    r >> role->id >> role->account_name >> role->character_name >> role->metempsychosis >> role->level
      >> role->high_level >> access_level >> role->exp >> max_hp >> cur_hp >> max_mp >> cur_mp
      >> ac >> str >> con >> dex >> cha >> men >> wis >> role->status >> role->career >> sex >> face
      >> role->x >> role->y >> role->map_id >> role->food >> justice >> role->title >> role->clan_id
      >> role->clan_class >> role->bonus_status >> role->elixir_status >> role->elf_attr >> role->exp_rec >> role->partner_id
      >> online_status >> role->hometown_id >> role->contribution >> role->pay >> role->hell_stay_time >> banned
      >> role->karma >> role->pk_count >> role->pk_count_for_elf >> role->last_pk >> role->last_pk_for_elf >> role->deadline
      >> role->original_str >> role->original_con >> role->original_dex >> role->original_cha >> role->original_men >> role->original_wis
      >> role->last_active >> role->ain_zone >> role->ain_point >> role->honor >> role->kills >> role->birthday;
    role->access_level(access_level);
    role->max_hp(max_hp);
    role->cur_hp(cur_hp);
    role->max_mp(max_mp);
    role->cur_mp(cur_mp);
    role->ac(ac);
    role->str(str);
    role->con(con);
    role->dex(dex);
    role->cha(cha);
    role->men(men);
    role->wis(wis);
    role->sex = (sex != 0);
    role->face(face);
    role->justice(justice);
    role->online_status = (online_status != 0);
    role->banned = (banned != 0);
    roles.push_back(role);
  }

  LOG_DEBUG << "Character::query_by_account " << account_name << " -> " << roles.size();
  return roles;
}

void Character::update(std::shared_ptr<def::Character> role) {
  LOG_DEBUG << "Character::update " << role->account_name << " -> " << role->character_name;
  session sql(ConnectionPoolManager::instance());
  int sex = int(role->sex);
  int online_status = int(role->online_status);
  int banned = int(role->banned);
  sql << "update characters set account_name = :account_name, character_name = :character_name, metempsychosis = :metempsychosis, level = :level, high_level = :high_level, access_level = :access_level, "
         "exp = :exp, max_hp = :max_hp, cur_hp = :cur_hp, max_mp = :max_mp, cur_mp = :cur_mp, ac = :ac, str = :str, con = :con, dex = :dex, cha = :cha, men = :men, wis = :wis, status = :status, career = :career, "
         "sex = :sex, face = :face, x = :x, y = :y, map_id = :map_id, food = :food, justice = :justice, title = :title, clan_id = :clan_id, clan_class = :clan_class, bonus_status = :bonus_status, "
         "elixir_status = :elixir_status, elf_attr = :elf_attr, exp_rec = :exp_rec, partner_id = :partner_id, online_status = :online_status, hometown_id = :hometown_id, contribution = :contribution, pay = :pay, "
         "hell_stay_time = :hell_stay_time, banned = :banned, karma = :karma, pk_count = :pk_count, pk_count_for_elf = :pk_count_for_elf, last_pk = :last_pk, last_pk_for_elf = :last_pk_for_elf, deadline = :deadline, "
         "original_str := original_str, original_con = :original_con, original_dex = :original_dex, original_cha = :original_cha, original_men = :original_men, original_wis := original_wis, "
         "last_active := last_active, ain_zone = :ain_zone, ain_point = :ain_point, honor = :honor, kills = :kills, birthday = :birthday"
         "where id = :id",
         use(role->account_name), use(role->character_name), use(role->metempsychosis), use(role->level), use(role->high_level), use(role->access_level()),
         use(role->exp), use(role->max_hp()), use(role->cur_hp()), use(role->max_mp()), use(role->cur_mp()), use(role->ac()), use(role->str()), use(role->con()), use(role->dex()), use(role->cha()), use(role->men()), use(role->wis()), use(role->status), use(role->career),
         use(sex), use(role->face()), use(role->x), use(role->y), use(role->map_id), use(role->food), use(role->justice()), use(role->title), use(role->clan_id), use(role->clan_class), use(role->bonus_status),
         use(role->elixir_status), use(role->elf_attr), use(role->exp_rec), use(role->partner_id), use(online_status), use(role->hometown_id), use(role->contribution), use(role->pay),
         use(role->hell_stay_time), use(banned), use(role->karma), use(role->pk_count), use(role->pk_count_for_elf), use(role->last_pk), use(role->last_pk_for_elf), use(role->deadline),
         use(role->original_str), use(role->original_con), use(role->original_dex), use(role->original_cha), use(role->original_men), use(role->original_wis),
         use(role->last_active), use(role->ain_zone), use(role->ain_point), use(role->honor), use(role->kills), use(role->birthday), use(role->id);
}

std::vector<std::string> Character::delete_expired(std::string &account_name) {
  LOG_DEBUG << "Character::delete_expired " << account_name;
  session sql(ConnectionPoolManager::instance());
  std::tm now;
  std::time_t t = std::time(nullptr);
  now = *std::localtime(&t);
  std::vector<std::string> character_names;
  rowset<row> rs = (sql.prepare << "select character_name from characters where account_name = :account_name and deadline >= :deadline", use(account_name), use(now));
  for (rowset<row>::const_iterator iter = rs.begin(); iter != rs.end(); ++iter) {
    const row &r = *iter;
    std::string character_name;
    r >> character_name;
    character_names.push_back(character_name);
  }
  sql << "delete from characters where account_name = :account_name and deadline >= :deadline", use(account_name), use(now);
  LOG_DEBUG << "Character::delete_expired " << account_name << " -> " << character_names.size();
  return character_names;
}

}
}