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

"""Test suite for the job dataclasses."""

import logging
import pytest

from wordcab.core_objects import BaseJob, ExtractJob, JobSettings, Source, SummarizeJob


@pytest.fixture
def dummy_job() -> BaseJob:
    """Fixture for a dummy Job object."""
    return BaseJob(
        display_name="Dummy Job",
        job_name="dummy_job",
        settings=JobSettings(),
        source=Source(source_type="generic"),
        time_started="dummy_time",
        transcript_id="dummy_transcript",
    )


@pytest.fixture
def dummy_extract_job() -> ExtractJob:
    """Fixture for a dummy ExtractJob object."""
    return ExtractJob(
        display_name="Dummy Extract Job",
        job_name="dummy_extract_job",
        settings=JobSettings(),
        source=Source(source_type="generic"),
        time_started="dummy_time",
        transcript_id="dummy_transcript",
    )


@pytest.fixture
def dummy_summarize_job() -> SummarizeJob:
    """Fixture for a dummy SummarizeJob object."""
    return SummarizeJob(
        display_name="Dummy Summarize Job",
        job_name="dummy_summarize_job",
        settings=JobSettings(),
        source=Source(source_type="generic"),
        time_started="dummy_time",
        transcript_id="dummy_transcript",
    )


@pytest.fixture
def empty_job_settings() -> JobSettings:
    """Fixture for an empty JobSettings object."""
    return JobSettings()


def test_dummy_job(dummy_job: BaseJob) -> None:
    """Test for a dummy Job object."""
    assert dummy_job is not None
    assert dummy_job.display_name == "Dummy Job"
    assert dummy_job.job_name == "dummy_job"
    assert dummy_job.job_status == "Pending"
    assert dummy_job.settings is not None
    assert dummy_job.source == Source(source_type="generic")
    assert dummy_job.time_started == "dummy_time"
    assert dummy_job.transcript_id == "dummy_transcript"
    
    assert hasattr(dummy_job, "job_update") and callable(getattr(dummy_job, "job_update"))


def test_job_update(dummy_job: BaseJob, caplog) -> None:
    """Test for the job_update method."""
    assert dummy_job.job_update is not None
    assert callable(dummy_job.job_update)
    with caplog.at_level(logging.INFO):
        dummy_job.job_update(source="dummy_source")
        assert dummy_job.source == "dummy_source"
        assert "Job dummy_job updated: source = dummy_source" in caplog.text
    with caplog.at_level(logging.INFO):
        before_status = dummy_job.job_status
        assert before_status == "Pending"
        dummy_job.job_update(job_status="Pending")
        assert dummy_job.job_status == before_status
        assert "Job dummy_job not updated: job_status = Pending" in caplog.text
    with pytest.raises(TypeError):
        dummy_job.job_update(
            {"time_started": "dummy_time", "transcript_id": "dummy_transcript", "job_status": "dummy_status"}
        )
    with caplog.at_level(logging.WARNING):
        dummy_job.job_update(new_jobsssss="new_jobsssss",)
        assert "Cannot update new_jobsssss in dummy_job, not a valid attribute." in caplog.text


def test_dummy_extract_job(dummy_extract_job: ExtractJob) -> None:
    """Test for a dummy ExtractJob object."""
    assert dummy_extract_job is not None
    assert dummy_extract_job.display_name == "Dummy Extract Job"
    assert dummy_extract_job.job_name == "dummy_extract_job"
    assert dummy_extract_job.job_status == "Pending"
    assert dummy_extract_job.settings is not None
    assert dummy_extract_job.source == Source(source_type="generic")
    assert dummy_extract_job.time_started == "dummy_time"
    assert dummy_extract_job.transcript_id == "dummy_transcript"

    assert dummy_extract_job._job_type == "ExtractJob"
    assert dummy_extract_job.AVAILABLE_STATUS is not None
    assert dummy_extract_job.AVAILABLE_STATUS == [
        "Deleted", "Error", "Extracting", "ExtractionComplete", "ItemQueued", "Pending", "PreparingExtraction",
    ]
    
    assert hasattr(dummy_extract_job, "job_update") and callable(getattr(dummy_extract_job, "job_update"))


def test_dummy_summarize_job(dummy_summarize_job: SummarizeJob) -> None:
    """Test for a dummy SummarizeJob object."""
    assert dummy_summarize_job is not None
    assert dummy_summarize_job.display_name == "Dummy Summarize Job"
    assert dummy_summarize_job.job_name == "dummy_summarize_job"
    assert dummy_summarize_job.job_status == "Pending"
    assert dummy_summarize_job.settings is not None
    assert dummy_summarize_job.source == Source(source_type="generic")
    assert dummy_summarize_job.time_started == "dummy_time"
    assert dummy_summarize_job.transcript_id == "dummy_transcript"

    assert dummy_summarize_job._job_type == "SummarizeJob"
    assert dummy_summarize_job.AVAILABLE_STATUS is not None
    assert dummy_summarize_job.AVAILABLE_STATUS == [
        "Deleted",
        "Error",
        "ItemQueued",
        "Pending",
        "PreparingSummary",
        "PreparingTranscript",
        "Summarizing",
        "SummaryComplete",
        "Transcribing",
        "TranscriptComplete",
    ]
    
    assert hasattr(dummy_summarize_job, "job_update") and callable(getattr(dummy_summarize_job, "job_update"))


def test_empty_job_settings(empty_job_settings: JobSettings) -> None:
    """Test for an empty JobSettings object."""
    assert empty_job_settings is not None
    assert empty_job_settings.ephemeral_data is False
    assert empty_job_settings.pipeline is None
    assert empty_job_settings.only_api is True
    assert empty_job_settings.split_long_utterances is False
