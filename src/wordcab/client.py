# coding=utf-8
# Copyright 2022 The Wordcab Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wordcab API Client."""

import os
from typing import Optional


class Client(object):
    """Wordcab API Client."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the client."""
        self.api_key = api_key if api_key else os.getenv("WORDCAB_API_KEY")
        if not self.api_key:
            # TODO: Add a better error message with cli login instructions
            raise ValueError("API Key not found. You must set the WORDCAB_API_KEY environment variable.")

    def __enter__(self):
        """Enter the client context."""
        return self

    def __exit__(self):
        """Exit the client context."""
        self.close()

    def close(self):
        """Close the client."""
        pass

    def get_stats(self):
        """Get the stats of the account."""
        raise NotImplementedError

    def start_extract(self):
        """Start an Extraction job."""
        raise NotImplementedError

    def start_summary(self):
        """Start a Summary job."""
        raise NotImplementedError

    def list_jobs(self):
        """List all jobs."""
        raise NotImplementedError

    def retrieve_job(self):
        """Retrieve a job."""
        raise NotImplementedError

    def delete_job(self):
        """Delete a job."""
        raise NotImplementedError

    def list_transcripts(self):
        """List all transcripts."""
        raise NotImplementedError

    def retrieve_transcript(self):
        """Retrieve a transcript."""
        raise NotImplementedError

    def change_speaker_labels(self):
        """Change the speaker labels of a transcript."""
        raise NotImplementedError

    def list_summaries(self):
        """List all summaries."""
        raise NotImplementedError

    def retrieve_summary(self):
        """Retrieve a summary."""
        raise NotImplementedError
