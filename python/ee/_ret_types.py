"""Internal types used to represent return values from the API."""

from __future__ import annotations

from typing import TypeVar

from ee import classifier
from ee import clusterer
from ee import computedobject
from ee import confusionmatrix
from ee import daterange
from ee import dictionary
from ee import ee_array
from ee import ee_date
from ee import ee_list
from ee import ee_number
from ee import ee_string
from ee import element
from ee import errormargin
from ee import featurecollection
from ee import filter as ee_filter
from ee import image
from ee import imagecollection
from ee import kernel
from ee import projection
from ee import reducer

ComputedObject = TypeVar(
    'ComputedObject',
    computedobject.ComputedObject,
    classifier.Classifier,
    clusterer.Clusterer,
    confusionmatrix.ConfusionMatrix,
    daterange.DateRange,
    dictionary.Dictionary,
    ee_array.Array,
    ee_date.Date,
    ee_filter.Filter,
    ee_list.List,
    ee_number.Number,
    ee_string.String,
    element.Element,
    errormargin.ErrorMargin,
    featurecollection.FeatureCollection,
    image.Image,
    imagecollection.ImageCollection,
    kernel.Kernel,
    projection.Projection,
    reducer.Reducer,
)
