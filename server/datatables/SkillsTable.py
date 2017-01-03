# -*- coding: utf-8 -*-

import logging
from Datatables import Session,skills,character_skills
from server.model.World import World
from server.templates.Skills import Skills
from server.utils.Singleton import Singleton

class SkillsTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._skills = {}
        self.LoadSkills()

    def LoadSkills(self):
        '''
        加载魔法清单到内存中
        :return:None
        '''
        with Session() as session:
            for rs in session.query(skills).all():
                item = Skills()
                item._skillId = rs.skill_id
                item._name = rs.name
                item._skillLevel = rs.skill_level
                item._skillNumber = rs.skill_number
                item._mpConsume = rs.mpConsume
                item._hpConsume = rs.hpConsume
                item._itmeConsumeId = rs.itemConsumeId
                item._itmeConsumeCount = rs.itemConsumeCount
                item._reuseDelay = rs.reuseDelay
                item._buffDuration = rs.buffDuration
                item._target = rs.target
                item._targetTo = rs.target_to
                item._damageValue = rs.damage_value
                item._damageDice = rs.damage_dice
                item._damageDiceCount = rs.damage_dice_count
                item._probabilityValue = rs.probability_value
                item._probabilityDice = rs.probability_dice
                item._attr = rs.attr
                item._type = rs.type
                item._lawful = rs.lawful
                item._ranged = rs.ranged
                item._area = rs.area
                item._isThrough = rs.through
                item._id = rs.id
                item._nameId = rs.nameid
                item._actionId = rs.action_id
                item._castGfx = rs.castgfx
                item._castGfx2 = rs.castgfx2
                item._sysmsgIdHappen = rs.sysmsgID_happen
                item._sysmsgIdStop = rs.sysmsgID_stop
                item._sysmsgIdFail = rs.sysmsgID_fail
                self._skills[item._skillId] = item
        logging.info("魔法清单共 " + str(len(self._skills)) + "件")

    def spellCheck(self, playerobjid, skillid):
        with Session() as session:
            rs = session.query(character_skills).filter(character_skills.char_obj_id == playerobjid,
                                                        character_skills.skill_id == skillid).one_or_none()
            if not rs:
                return False
        return True

    def spellMastery(self, playerobjid, skillid, skillname, active, time):
        if self.spellCheck(playerobjid, skillid):
            return

        if World()._allObjects.has_key(playerobjid):
            World()._allObjects[playerobjid].setSkillMastery(skillid)

        with Session() as session:
            item = character_skills()
            item.char_obj_id = playerobjid
            item.skill_id = skillid
            item.skill_name = skillname
            item.is_active = active
            item.activetimeleft = time
            session.add(item)

    def spellLost(self, playerobjid, skillid):
        if World()._allObjects.has_key(playerobjid):
            World()._allObjects[playerobjid].removeSkillMastery(skillid)

        with Session() as session:
            session.query(character_skills).filter(character_skills.char_obj_id == playerobjid,
                                                   character_skills.skill_id == skillid).delete()