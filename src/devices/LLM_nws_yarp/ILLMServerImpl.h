/*
 * SPDX-FileCopyrightText: 2023-2023 Istituto Italiano di Tecnologia (IIT)
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <yarp/dev/llm/ILLMMsgs.h>
#include <yarp/dev/ILLM.h>

class ILLMRPCd : public yarp::dev::llm::ILLMMsgs
{
private:
    yarp::dev::ILLM *m_iLlm = nullptr;

public:
    void setInterface(yarp::dev::ILLM *_iLlm) { m_iLlm = _iLlm; }
    // From IGPTMsgs
    bool setPrompt(const std::string &prompt) override;
    yarp::dev::llm::return_readPrompt readPrompt() override;
    yarp::dev::llm::return_ask ask(const std::string &question) override;
    yarp::dev::llm::return_getConversation getConversation() override;
    bool deleteConversation() override;
};
