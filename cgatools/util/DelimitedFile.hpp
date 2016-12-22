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

#ifndef CGATOOLS_UTIL_DELIMITEDFILE_HPP_
#define CGATOOLS_UTIL_DELIMITEDFILE_HPP_ 1

//! @file DelimitedFile.hpp

#include "cgatools/core.hpp"
#include "cgatools/util/DelimitedLineParser.hpp"

#include <boost/noncopyable.hpp>

namespace cgatools { namespace util {

    class DelimitedFileMetadata
    {
    public:
        //! Format version for the output files generated by this executable
        static const std::string OUTPUT_FORMAT_VERSION;

        //! The value that goes into SOFTWARE_VERSION if this version of
        //! cgatools is being run in the pipeline. Otherwise, this
        //! string is empty.
        static std::string PIPELINE_VERSION;

        //! Returns CGI format version for this metadata set.
        //! The version is returned as MAJOR * 1000 + MINOR, that is, for
        //! format version "1.2" this returns 1002.
        //! When the version cannot be detected, throws an exception.
        int getFormatVersion() const;

        //! Returns the SRC_SOFTWARE_VERSION for this file metadata. If
        //! there is no SRC_SOFTWARE_VERSION, returns the
        //! SOFTWARE_VERSION. If neither exists, returns the value for
        //! key BUILD. If none of these exists, returns "".
        std::string getSoftwareVersionString() const;

        bool hasKey(const std::string& key) const;
        const std::string& get(const std::string& key) const;
        template <class T>
        const T get(const std::string& key) const {
            return util::parseValue<T>(get(key));
        }

        void set(const std::string& key, const std::string& value);
        void add(const std::string& key, const std::string& value);
        void removeAll(const std::string& key);

        const std::vector< std::pair<std::string, std::string> >& getMap() const
        {
            return kv_;
        }

        //! Fills in GENERATED_BY, GENERATED_AT, CGATOOLS_VERSION (or
        //! SOFTWARE_VERSION, if this version of cgatools is being run
        //! in the pipeline), and FORMAT_VERSION. Also transfers the
        //! SOFTWARE_VERSION and all the other keys not listed above from the
        //! input DelimitedFileMetadata object.
        void initDefaults(const DelimitedFileMetadata& meta = DelimitedFileMetadata());

        //! Transfer specified keys from another metadata store, optionally
        //! attaching a specified prefix to each key
        void transfer(const DelimitedFileMetadata& src,
                      const std::string& keys,
                      const std::string& prefix = "");

        //! Sorts the lines
        void sort();

        void setFileName(const std::string& fn)
        {
            fileName_ = fn;
        }


        const std::string & getFileName() const{
            return fileName_;
        }

    private:
        std::vector< std::pair<std::string, std::string> > kv_;
        std::string fileName_;

        void reportError(const std::string& error) const;
    };

    std::ostream& operator<< (std::ostream& out, const DelimitedFileMetadata& meta);

    //! Used to parse files delimited in the way found in a typical
    //! Complete Genomics data file. Example:
    //! @code
    //! string chromosome;
    //! uint32_t offset;
    //! DelimitedFile df(cin);
    //! df.addField(StringField("chromosome", &chromosome));
    //! df.addField(ValueField<uint32_t>("offset", &offset));
    //! while (df.next())
    //!     cout << chromosome << "\t" << offset << endl;
    //! @endcode
    class DelimitedFile : boost::noncopyable
    {
    public:
        typedef DelimitedFileMetadata Metadata;
        typedef DelimitedLineParser::EmptyFieldHandling EmptyFieldHandling;
        typedef DelimitedLineParser::StrictnessChecking StrictnessChecking;

        explicit DelimitedFile(
            std::istream& in,
            const std::string& fileName /* = "unknown" */,
            char delimiter = '\t',
            EmptyFieldHandling emptyHandling = DelimitedLineParser::PROCESS_EMPTY_FIELDS,
            StrictnessChecking strictnessChecking = DelimitedLineParser::RELAXED_CHECKING);

        enum FieldParserType
        {
            FPT_REQUIRED = 0,
            FPT_OPTIONAL = 1
        };
        template <class Field>
        void addField(const Field& parser, FieldParserType ft = FPT_REQUIRED)
        {
            int count = 0;
            for(size_t ii=0; ii<columnHeaders_.size(); ii++)
            {
                if (columnHeadersEqual(columnHeaders_[ii], parser.getName()))
                {
                    lp_.setField(ii, parser);
                    count++;
                }
            }
            if (0 == count && FPT_OPTIONAL != ft)
                reportError("missing required field: "+parser.getName());
            if (count > 1)
                reportError("multiple fields with same name: "+parser.getName());
        }

        void addAllFields(std::vector<std::string>& fields);

        bool next();

        const Metadata& getMetadata() const
        {
            return metadata_;
        }

        const std::vector<std::string>& getColumnHeaders() const
        {
            return columnHeaders_;
        }

        size_t getFieldOffset(const std::string& fieldName) const;

        bool hasField(const std::string& fieldName) const;

        DelimitedLineParser& getDelimitedLineParser()
        {
            return lp_;
        }

        const std::string& getLine() const
        {
            return line_;
        }

    private:
        void readHeader();
        void reportError(const std::string& error) const;
        bool columnHeadersEqual(const std::string& h1, const std::string& h2) const;

        std::istream& in_;
        std::string fileName_;
        Metadata metadata_;
        std::vector<std::string> columnHeaders_;
        DelimitedLineParser lp_;
        std::string line_;
        char delimiter_;
        EmptyFieldHandling emptyHandling_;
        StrictnessChecking strictnessChecking_;
        size_t lineNo_;
        std::string activeLineSetId_;
        bool withinActiveLineSet_;
    };

} } // cgatools::util

#endif // CGATOOLS_UTIL_DELIMITEDFILE_HPP_
