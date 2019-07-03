//
// Created by 范炜东 on 2019/6/29.
//

#include "StateMachine.h"

std::shared_ptr<EventData> NoEventData = std::make_shared<EventData>();

//----------------------------------------------------------------------------
// StateMachine
//----------------------------------------------------------------------------
StateMachine::StateMachine(unsigned char maxStates, unsigned char initialState) :
        MAX_STATES(maxStates),
        m_currentState(initialState),
        m_newState(FALSE),
        m_eventGenerated(FALSE),
        m_pEventData(NULL)
{
  ASSERT_TRUE(MAX_STATES < EVENT_IGNORED);
}

//----------------------------------------------------------------------------
// ExternalEvent
//----------------------------------------------------------------------------
void StateMachine::ExternalEvent(unsigned char newState, const std::shared_ptr<EventData> pData)
{
  // If we are supposed to ignore this event
  if (newState != EVENT_IGNORED)
  {
    // TODO - capture software lock here for thread-safety if necessary

    m_newState = newState;

    // Execute the state engine. This function call will only return
    // when all state machine events are processed.
    StateEngine();

    // TODO - release software lock here
  }
}

//----------------------------------------------------------------------------
// StateEngine
//----------------------------------------------------------------------------
void StateMachine::StateEngine(void, const std::shared_ptr<EventData> pData)
{
  const StateMapRow* pStateMap = GetStateMap();
  if (pStateMap != nullptr)
    StateEngine(pStateMap, pData);
  else
  {
    const StateMapRowEx* pStateMapEx = GetStateMapEx();
    if (pStateMapEx != nullptr)
      StateEngine(pStateMapEx, pData);
    else
      ASSERT();
  }
}

//----------------------------------------------------------------------------
// StateEngine
//----------------------------------------------------------------------------
void StateMachine::StateEngine(const StateMapRow* const pStateMap, const std::shared_ptr<EventData> pData)
{
  // Error check that the new state is valid before proceeding
  ASSERT_TRUE(m_newState < MAX_STATES);

  // Get the pointer from the state map
  const StateBase* state = pStateMap[m_newState].State;

  // Switch to the new current state
  SetCurrentState(m_newState);

  // Execute the state action passing in event data
  ASSERT_TRUE(state != nullptr);
  state->InvokeStateAction(this, pData);
}

//----------------------------------------------------------------------------
// StateEngine
//----------------------------------------------------------------------------
void StateMachine::StateEngine(const StateMapRowEx* const pStateMapEx, const std::shared_ptr<EventData> pData)
{
  // Error check that the new state is valid before proceeding
  ASSERT_TRUE(m_newState < MAX_STATES);

  // Get the pointers from the state map
  const StateBase* state = pStateMapEx[m_newState].State;
  const GuardBase* guard = pStateMapEx[m_newState].Guard;
  const EntryBase* entry = pStateMapEx[m_newState].Entry;
  const ExitBase* exit = pStateMapEx[m_currentState].Exit;

  // Execute the guard condition
  bool guardResult = true;
  if (guard != NULL)
    guardResult = guard->InvokeGuardCondition(this, pData);

  // If the guard condition succeeds
  if (guardResult)
  {
    // Transitioning to a new state?
    if (m_newState != m_currentState)
    {
      // Execute the state exit action on current state before switching to new state
      if (exit != nullptr)
        exit->InvokeExitAction(this);

      // Execute the state entry action on the new state
      if (entry != nullptr)
        entry->InvokeEntryAction(this, pData);
    }

    // Switch to the new current state
    SetCurrentState(m_newState);

    // Execute the state action passing in event data
    ASSERT_TRUE(state != nullptr);
    state->InvokeStateAction(this, pData);
  }
}