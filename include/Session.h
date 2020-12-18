//
// Created by kyle on 2020/12/22.
//

#ifndef KGE_SESSION_H
#define KGE_SESSION_H

#include <memory>

namespace kge {

class Connect;
class Session : public std::enable_shared_from_this<Session> {
public:
  Session(std::shared_ptr<Connect> connection);
  virtual ~Session();

protected:
  std::shared_ptr<Connect> connection_;
};

}
#endif //KGE_SESSION_H
