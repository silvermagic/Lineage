#ifndef TOBJECT_H
#define TOBJECT_H

#include "model/TLocation.h"

class TObject
{
public:
  TObject();
  virtual ~TObject();

  /** 获取与另一个对象的直线距离 */
  double getLineDistance(const TObject& obj);
  /** 获取对象所在位置 */
  const TLocation& getLocation();
  /** 获取对象所在地图 */
  const std::shared_ptr<TMap> getMap();
  /** 获取对象所在地图ID */
  unsigned int getMapId();
  /** 取得与另一个对象间的X轴+Y轴的距离 */
  int getTileDistance(const TObject& obj);
  /** 取得与另一个对象间的X轴或Y轴距离较大值 */
  int getTileLineDistance(const TObject& obj);
  /** 取得对象在地图上的X轴值 */
  int getX();
  /** 取得对象在地图上的Y轴值 */
  int getY();

  /** 玩家对对象采取行动时，对象的响应 */
  void onAction(const TObject& actionFrom);
  /** 玩家对对象释放技能时，对象的响应 */
  void onAction(const TObject& actionFrom, unsigned int skillId);
  /** 玩家进入对象屏幕范围时，对象的响应 */
  void onPerceive(const TObject& perceivedFrom);
  /** 玩家与对象进行交谈时，对象的响应 */
  void onTalkAction(const TObject& talkFrom);

  /** 设定对象在世界中唯一的ID */
  void setId(unsigned int id);
  /** 设置对象存在在地图上的坐标 */
  void setLocation(int x, int y, unsigned int mapid);
  /** 设置对象存在在地图上的坐标 */
  void setLocation(const TLocation& loc);
  /** 设定对象所存在的地图ID */
  void setMap(unsigned int mapId);
  /** 设定对象所存在的地图 */
  void setMap(std::shared_ptr<TMap> map);
  /** 设定对象在地图上的X轴值 */
  void setX(int x);
  /** 设定对象在地图上的Y轴值 */
  void setY(int y);

protected:
  TLocation _loc;
  unsigned int _id;
};

#endif // TOBJECT_H
