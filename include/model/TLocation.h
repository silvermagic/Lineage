#ifndef TLOCATION_H
#define TLOCATION_H

#include <memory>
#include "types/TPoint.h"

class L1Map;

class TLocation : public TPoint
{
public:
  TLocation();
  TLocation(int x, int y, int mapId);
  TLocation(int x, int y, std::shared_ptr<L1Map> map);
  TLocation(const TLocation&);
  TLocation(const TPoint& pt, int mapId);
  TLocation(const TPoint& pt, std::shared_ptr<L1Map> map);
  virtual ~TLocation();

  /** 位置是否相同 */
  bool equals(const TLocation& loc);
  /** 获取位置所属地图 */
  const std::shared_ptr<L1Map> geL1Map();
  /** 获取位置所属地图ID */
  unsigned int geL1MapId();
  /** 获取对象的hash值 */
  int hashCode();

  /**
  * 返回原位置在范围内随机移动后的新位置
  *
  * @param baseLocation
  *            随机移动前的位置
  * @param min
  *            随机移动范围的最小值(0包含自身的坐标)
  * @param max
  *            随机移动范围的最大值
  * @param isRandomTeleport
  *            是否随机传送
  * @return 随机移动后的新位置
  */
  static TLocation randomLocation(TLocation& baseLocation, int min, int max, bool isRandomTeleport);
  /** 获取当前位置随机移动后的位置 */
  TLocation randomLocation(int max, bool isRandomTeleport);
  TLocation randomLocation(int min, int max, bool isRandomTeleport);

  /** 设置当前位置 */
  void set(int x, int y, int mapId);
  void set(int x, int y, std::shared_ptr<L1Map> map);
  void set(const TLocation& loc);
  void set(const TPoint& pt, unsigned int mapId);
  void set(const TPoint& pt, std::shared_ptr<L1Map> map);
  void seL1Map(unsigned int mapId);
  void seL1Map(std::shared_ptr<L1Map> map);

  std::string toString();

protected:
  std::shared_ptr<L1Map> _map;
};

#endif // TLOCATION_H
