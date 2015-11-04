#ifndef TMAP_H
#define TMAP_H

/**
* 从框架的角度看,地图类核心功能就是判断两点之间是否存在障碍影响行走或攻击
*/

#include <string>
#include <memory>

class TPoint;

class TMap
{
public:
  static std::shared_ptr<TMap> newNull();
  virtual ~TMap();

  virtual int getId() = 0;
	virtual int getX() = 0;
	virtual int getY() = 0;
	virtual int getWidth() = 0;
	virtual int getHeight() = 0;
	virtual int getTile(int x, int y) = 0;
	virtual int getOriginalTile(int x, int y) = 0;

	/** 判断点是否在地图范围内 */
	virtual bool isInMap(const TPoint& pt) = 0;
	virtual bool isInMap(int x, int y) = 0;
  /** 判断地图上的点玩家是否可以穿过 */
	virtual bool isPassable(const TPoint& pt) = 0;
	virtual bool isPassable(int x, int y) = 0;
	virtual bool isPassable(const TPoint& pt, int heading) = 0;
	virtual bool isPassable(int x, int y, int heading) = 0;
	/** 判断地图上的点箭矢是否可以穿过 */
	virtual bool isArrowPassable(const TPoint& pt) = 0;
	virtual bool isArrowPassable(int x, int y) = 0;
	virtual bool isArrowPassable(const TPoint& pt, int heading) = 0;
	virtual bool isArrowPassable(int x, int y, int heading) = 0;
  /** 判断地图上的点是否为安全区域 */
	virtual bool isSafetyZone(const TPoint& pt) = 0;
	virtual bool isSafetyZone(int x, int y) = 0;
	/** 判断地图上的点是否为战斗区域 */
	virtual bool isCombatZone(const TPoint& pt) = 0;
	virtual bool isCombatZone(int x, int y) = 0;
	/** 判断地图上的点是否为一般区域 */
	virtual bool isNormalZone(const TPoint& pt) = 0;
	virtual bool isNormalZone(int x, int y) = 0;
  /** 地图是否在水下 */
	virtual bool isUnderwater() = 0;
	/** 地图是否允许记忆坐标 */
	virtual bool isMarkable() = 0;
	/** 地图是否在水下 */
	virtual bool isTeleportable() = 0;
	/** 地图是否允许使用传送回家卷轴 */
	virtual bool isEscapable() = 0;
	/** 地图是否允许使用复活卷轴 */
	virtual bool isUseResurrection() = 0;
	virtual bool isUsePainwand() = 0;
	/** 地图是否有死亡惩罚 */
	virtual bool isEnabledDeathPenalty() = 0;
	/** 地图是否允许携带宠物 */
	virtual bool isTakePets() = 0;
	/** 地图是否允许召唤宠物 */
	virtual bool isRecallPets() = 0;
	/** 地图是否允许使用道具 */
	virtual bool isUsableItem() = 0;
	/** 地图是否允许使用技能 */
	virtual bool isUsableSkill() = 0;
	/** 地图对应位置是否可以钓鱼 */
	virtual bool isFishingZone(int x, int y) = 0;
	/** 地图对应位置是否有门 */
	virtual bool isExistDoor(int x, int y) = 0;

	/** 设置地图对应位置是否可穿过 */
	virtual void setPassable(const TPoint& pt, bool isPassable) = 0;
	virtual void setPassable(int x, int y, bool isPassable) = 0;

	/** 地图对应位置的文字描述 */
	virtual std::string toString(const TPoint& pt) = 0;
  /** 是否为空地图 */
	virtual bool isNull();

protected:
  TMap();
};

class TNullMap : public TMap
{
public:
  TNullMap();
  virtual ~TNullMap();

  int getId();
  int getX();
	int getY();
	int getWidth();
	int getHeight();
	int getTile(int x, int y);
	int getOriginalTile(int x, int y);
	bool isInMap(const TPoint& pt);
	bool isInMap(int x, int y);
	bool isPassable(const TPoint& pt);
	bool isPassable(int x, int y);
	bool isPassable(const TPoint& pt, int heading);
	bool isPassable(int x, int y, int heading);
	bool isArrowPassable(const TPoint& pt);
	bool isArrowPassable(int x, int y);
	bool isArrowPassable(const TPoint& pt, int heading);
	bool isArrowPassable(int x, int y, int heading);
	bool isSafetyZone(const TPoint& pt);
	bool isSafetyZone(int x, int y);
	bool isCombatZone(const TPoint& pt);
	bool isCombatZone(int x, int y);
	bool isNormalZone(const TPoint& pt);
	bool isNormalZone(int x, int y);
	bool isUnderwater();
	bool isMarkable();
	bool isTeleportable();
	bool isEscapable();
	bool isUseResurrection();
	bool isUsePainwand();
	bool isEnabledDeathPenalty();
	bool isTakePets();
	bool isRecallPets();
	bool isUsableItem();
	bool isUsableSkill();
	bool isFishingZone(int x, int y);
	bool isExistDoor(int x, int y);
	void setPassable(const TPoint& pt, bool isPassable);
	void setPassable(int x, int y, bool isPassable);
  std::string toString(const TPoint& pt);
	bool isNull();
};

#endif // TMAP_H
