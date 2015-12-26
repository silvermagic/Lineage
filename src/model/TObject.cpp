#include "model/TObject.h"

TObject::TObject()
{
}

TObject::~TObject()
{
}

double TObject::getLineDistance(const TObject& obj)
{
  return 0.0;
}

const TLocation& TObject::getLocation()
{
  return _loc;
}

const std::shared_ptr<L1Map> TObject::geL1Map()
{
  return _loc.geL1Map();
}

unsigned int TObject::geL1MapId()
{
  return 0;
}

int TObject::getTileDistance(const TObject& obj)
{
  return 0;
}

int TObject::getTileLineDistance(const TObject& obj)
{
  return 0;
}

int TObject::getX()
{
  return 0;
}

int TObject::getY()
{
  return 0;
}

void TObject::onAction(const TObject& actionFrom)
{
}

void TObject::onAction(const TObject& actionFrom, unsigned int skillId)
{
}

void TObject::onPerceive(const TObject& perceivedFrom)
{
}

void TObject::onTalkAction(const TObject& talkFrom)
{
}


void TObject::setId(unsigned int id)
{
}

void TObject::setLocation(int x, int y, unsigned int mapid)
{
}

void TObject::setLocation(const TLocation& loc)
{
}

void TObject::seL1Map(unsigned int mapId)
{
}

void TObject::seL1Map(std::shared_ptr<L1Map> map)
{
}

void TObject::setX(int x)
{
}

void TObject::setY(int y)
{
}
