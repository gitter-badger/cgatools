// Copyright 2010 Complete Genomics, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License"); you
// may not use this file except in compliance with the License. You
// may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
// implied. See the License for the specific language governing
// permissions and limitations under the License.

#ifndef CGA_TOOLS_COMMAND_FASTA2CRR_HPP_
#define CGA_TOOLS_COMMAND_FASTA2CRR_HPP_ 1

//! @file Fasta2Crr.hpp

#include "cgatools/core.hpp"
#include "cgatools/command/Command.hpp"

namespace cgatools { namespace command {

    class Fasta2Crr : public Command
    {
    public:
        Fasta2Crr(const std::string& name);

    protected:
        int run(po::variables_map& vm);
        
    private:
        std::string parseFastaHeader(const std::string& line) const;

        std::vector<std::string> inputFileNames_;
        std::string outputFileName_;
        std::string circularChromosomes_;
    };

} } // cgatools::command

#endif // CGA_TOOLS_COMMAND_FASTA2CRR_HPP_
